import type { CollectionEntry } from 'astro:content';

/**
 * Único sitio donde se construyen URLs.
 *
 * Si algún día el formato cambia (`/ade/4/c1/` → `/ade/curso-4/cuatri-1/`),
 * se toca aquí y en ningún otro archivo.
 */

const BASE = import.meta.env.BASE_URL.replace(/\/?$/, '/');

export type Subject = CollectionEntry<'subjects'>;
export type Degree = CollectionEntry<'degrees'>;

/** `subjects/ade/rrhh` → `rrhh` */
export function subjectSlug(entry: Subject): string {
  return entry.id.split('/').pop()!;
}

/** `subjects/ade/rrhh` → `ade` */
export function degreeSlug(entry: Subject): string {
  return entry.data.degree.id;
}

/** Palabras que no cuentan al formar las siglas de una asignatura. */
const STOPWORDS = new Set(['de', 'del', 'la', 'las', 'los', 'el', 'y', 'en', 'a', 'i', 'ii']);

/**
 * Sigla corta para la cabecera del motor de tests: "MP", "OE", "SIBW".
 * Los slugs cortos ya son la sigla; los largos la sacan de las iniciales.
 */
export function subjectCode(entry: Subject): string {
  const slug = subjectSlug(entry);
  if (slug.length <= 5) return slug.toUpperCase();
  return (
    entry.data.title
      .split(/\s+/)
      .filter((w) => !STOPWORDS.has(w.toLowerCase()))
      .map((w) => w[0])
      .join('')
      .toUpperCase()
      .slice(0, 5) || slug.slice(0, 4).toUpperCase()
  );
}

export const degreePath = (degree: string) => `${BASE}${degree}/`;

export const yearPath = (degree: string, year: number) =>
  `${BASE}${degree}/${year}/`;

export const semesterPath = (degree: string, year: number, semester: number) =>
  `${BASE}${degree}/${year}/c${semester}/`;

export const subjectPath = (
  degree: string,
  year: number,
  semester: number,
  slug: string
) => `${BASE}${degree}/${year}/c${semester}/${slug}/`;

export const materialPath = (
  degree: string,
  year: number,
  semester: number,
  slug: string,
  material: string
) => `${subjectPath(degree, year, semester, slug)}${material}/`;

/**
 * A dónde lleva una asignatura.
 *
 * Las que viven en otro repo salen fuera; el resto van a su hub jerárquico,
 * que es quien enlaza el material. Devuelve `null` si aún no hay nada: en
 * ese caso la tarjeta se pinta apagada y lleva al issue de GitHub.
 */
export function subjectUrl(entry: Subject): string | null {
  const { external, status, year, semester } = entry.data;
  if (external) return external;
  if (status === 'available') {
    return subjectPath(degreeSlug(entry), year, semester, subjectSlug(entry));
  }
  return null;
}


/** Asignaturas que generan página propia (las externas no la necesitan). */
export function hasHub(entry: Subject): boolean {
  return entry.data.status === 'available' && !entry.data.external;
}

/** Issue de GitHub con grado, curso y cuatrimestre ya rellenos. */
export function contributeUrl(entry: Subject, degreeName: string): string {
  const body = [
    '## Datos',
    `- **Asignatura**: ${entry.data.title}`,
    `- **Grado**: ${degreeName}`,
    `- **Curso**: ${entry.data.year}º`,
    `- **Cuatrimestre**: ${entry.data.semester}`,
    '',
    '## Qué aporto',
    '- [ ] Tipo test',
    '- [ ] Verdadero/Falso',
    '- [ ] Flashcards',
    '- [ ] Apuntes en PDF',
  ].join('\n');

  return (
    'https://github.com/jxliian/repasaYA/issues/new' +
    `?title=${encodeURIComponent(`Material: ${entry.data.title}`)}` +
    `&body=${encodeURIComponent(body)}`
  );
}

/** Migas de pan de una asignatura, de la raíz hacia dentro. */
export function subjectCrumbs(entry: Subject, degreeShort: string) {
  const d = degreeSlug(entry);
  const { year, semester } = entry.data;
  return [
    { label: 'Inicio', href: BASE },
    { label: degreeShort, href: degreePath(d) },
    { label: `${year}º`, href: yearPath(d, year) },
    { label: `Cuatri ${semester}`, href: semesterPath(d, year, semester) },
    { label: entry.data.title, href: null },
  ];
}
