import { defineCollection, reference, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * Colecciones de contenido de repasaYA.
 *
 * Esto es la "API pública" para quien quiera contribuir: si un archivo
 * cumple el esquema, entra; si no, el build falla y el PR no se mergea.
 * Nadie necesita tocar un componente para añadir una asignatura.
 *
 * OJO con las rutas de archivo: `subjects/ade/rrhh.md` NO codifica el
 * curso ni el cuatrimestre. Eso vive en el frontmatter y la URL se compone
 * en `src/lib/routes.ts`. Así, mover una asignatura de cuatrimestre es
 * editar una línea, no reorganizar carpetas.
 */

/** Tipos de material que entiende la plataforma. */
export const MATERIAL_TYPES = [
  'test',
  'vf',
  'reveal',
  'flashcards',
  'glosario',
  'apuntes',
  'guia',
] as const;

const degrees = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/degrees' }),
  schema: z.object({
    name: z.string(),
    short: z.string(),
    icon: z.string(),
    years: z.number().int().min(1).max(6).default(4),
    accent: z.string(),
    blurb: z.string(),
  }),
});

const subjects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/subjects' }),
  schema: z.object({
    title: z.string(),
    degree: reference('degrees'),
    year: z.number().int().min(1).max(5),
    semester: z.union([z.literal(1), z.literal(2)]),
    credits: z.number().int().positive().default(6),
    icon: z.string().default('📘'),

    /**
     * available → tiene material publicado y es navegable
     * planned   → existe en el plan de estudios pero está vacía
     */
    status: z.enum(['available', 'planned']).default('planned'),

    description: z.string().optional(),
    difficulty: z.enum(['facil', 'media', 'dura']).optional(),

    /** Tipos de material disponibles. Alimenta los filtros del catálogo. */
    materials: z.array(z.enum(MATERIAL_TYPES)).default([]),

    /** La asignatura vive en otro repo (p. ej. Economía Española). */
    external: z.string().url().optional(),

  }),
});

/* ── Materiales ────────────────────────────────────────────────────
   Un archivo = un bloque de material de una asignatura. Es lo que
   abre un PR quien quiera contribuir, así que el esquema es estricto
   a propósito: si falta `correct` o una opción está vacía, el build
   falla y el fallo se ve antes de llegar a producción.            */

/** Pregunta tipo test: varias opciones, una correcta (índice, base 0). */
const testItem = z.object({
  tema: z.string(),
  q: z.string(),
  opts: z.array(z.string().min(1)).min(2),
  correct: z.number().int().min(0),
  justification: z.string().optional(),
});

/** Verdadero/Falso, con justificación cuando la hay. */
const vfItem = z.object({
  tema: z.string(),
  q: z.string(),
  answer: z.enum(['V', 'F']),
  justification: z.string().optional(),
  n: z.number().int().optional(),
});

/** Pregunta con respuesta abierta que se destapa al pulsar. */
const revealItem = z.object({
  tema: z.string(),
  q: z.string(),
  answer: z.string().min(1),
});

/** Tarjeta de memoria: término por delante, definición por detrás. */
const cardItem = z.object({
  tema: z.string(),
  term: z.string(),
  def: z.string(),
});

const materialBase = {
  subject: reference('subjects'),
  title: z.string(),
  /** Orden dentro del hub de la asignatura. Menor, antes. */
  order: z.number().int().default(0),
  /**
   * Genera página pero no se lista en ningún sitio ni se indexa.
   * Para material que solo se encuentra si te pasan el enlace.
   */
  hidden: z.boolean().default(false),
};

const materials = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/materials' }),
  schema: z.discriminatedUnion('type', [
    z.object({ ...materialBase, type: z.literal('test'), items: z.array(testItem).min(1) }),
    z.object({ ...materialBase, type: z.literal('vf'), items: z.array(vfItem).min(1) }),
    z.object({ ...materialBase, type: z.literal('reveal'), items: z.array(revealItem).min(1) }),
    z.object({
      ...materialBase,
      type: z.literal('flashcards'),
      items: z.array(cardItem).min(1),
    }),
    z.object({
      ...materialBase,
      type: z.literal('glosario'),
      items: z.array(cardItem).min(1),
    }),
    // Los apuntes no llevan preguntas: apuntan a un PDF de `public/`
    z.object({ ...materialBase, type: z.literal('apuntes'), pdf: z.string() }),
    // Una guía es una página propia: la colección solo guarda el enlace
    z.object({ ...materialBase, type: z.literal('guia'), href: z.string() }),
  ]),
});

export const collections = { degrees, subjects, materials };
