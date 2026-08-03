import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { degreeSlug, subjectSlug, subjectUrl } from '../lib/routes';

/**
 * Índice de búsqueda global, generado en build.
 *
 * Se sirve como archivo estático y el buscador lo pide la PRIMERA vez que
 * el usuario escribe. Así la landing no carga el índice hasta que hace
 * falta: con 64 asignaturas son ~14 KB que no lastran el primer pintado.
 */

const MATERIAL_LABEL: Record<string, string> = {
  test: 'Tipo test',
  vf: 'V/F',
  reveal: 'Quiz',
  flashcards: 'Flashcards',
  glosario: 'Glosario',
  apuntes: 'Apuntes',
  examen: 'Exámenes',
};

/** Quita tildes y baja a minúsculas: "Economía" y "economia" deben empatar. */
function normalize(s: string): string {
  return s
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '');
}

export const GET: APIRoute = async () => {
  const subjects = await getCollection('subjects');
  const degrees = await getCollection('degrees');
  const degreeById = new Map(degrees.map((d) => [d.id, d.data]));

  const items = subjects
    .sort((a, b) =>
      a.data.year - b.data.year ||
      a.data.semester - b.data.semester ||
      a.data.title.localeCompare(b.data.title, 'es')
    )
    .map((entry) => {
      const dSlug = degreeSlug(entry);
      const degree = degreeById.get(dSlug);
      const url = subjectUrl(entry);

      return {
        slug: subjectSlug(entry),
        title: entry.data.title,
        icon: entry.data.icon,
        degree: dSlug,
        degreeShort: degree?.short ?? dSlug,
        year: entry.data.year,
        semester: entry.data.semester,
        available: url !== null,
        // Las que aún no tienen material van sin URL: el buscador compone
        // el enlace al issue en cliente. Meterlo aquí, ya codificado y
        // repetido 56 veces, engordaba el índice un 45 %.
        url: url ?? '',
        external: Boolean(entry.data.external),
        materialLabels: entry.data.materials.map((m) => MATERIAL_LABEL[m] ?? m),
        // Todo lo buscable, aplanado y normalizado: una sola pasada en cliente
        haystack: normalize(
          [
            entry.data.title,
            subjectSlug(entry),
            degree?.short ?? '',
            degree?.name ?? '',
            entry.data.description ?? '',
            `${entry.data.year}º`,
            ...entry.data.materials.map((m) => MATERIAL_LABEL[m] ?? m),
          ].join(' ')
        ),
      };
    });

  return new Response(JSON.stringify({ items }), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
