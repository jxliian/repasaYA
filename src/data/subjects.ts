export type QuizType = 'vf' | 'test' | 'both';

export interface Subject {
  slug: string;          // URL: /repasaYA/RRHH/
  title: string;
  code: string;
  icon: string;
  description: string;
  type: QuizType;
  chips: string[];       // etiquetas bajo la card
  external?: string;     // si ya existe en otro repo
  dataFile?: string;     // nombre del json en src/data/
  quizFile?: string;     // json del quiz tipo test (opcional)
}

export const subjects: Subject[] = [
  {
    slug: 'economia-espanola',
    title: 'Economía Española',
    code: '4º · Economía',
    icon: '🇪🇸',
    description: 'Tests por tema, banco de preguntas, flashcards y exámenes oficiales.',
    type: 'test',
    chips: ['+300 preguntas', '9 temas'],
    external: 'https://jxliian.github.io/EE_tipotest/',
  },
  {
    slug: 'rrhh',
    title: 'Recursos Humanos',
    code: 'ADE · Empresa',
    icon: '👥',
    description: '318 V/F con justificación + 138 quiz tipo test. 11 bloques y exámenes.',
    type: 'both',
    chips: ['318 V/F', '138 quiz'],
    dataFile: 'rrhh.json',
  },
  {
    slug: 'organizacion-empresas',
    title: 'Organización de Empresas',
    code: 'ADE · Organización',
    icon: '🏢',
    description: '318 preguntas tipo test sobre Mintzberg. 18 bloques.',
    type: 'test',
    chips: ['318 preguntas', '18 bloques'],
    dataFile: 'oe.json',
  },
  {
    slug: 'do1',
    title: 'Dirección de Operaciones I',
    code: 'ADE · Operaciones',
    icon: '⚙️',
    description: '80 V/F con justificación. T1-T7: Intro, Cadena de Suministro, Diseño de Producto, Estrategia de Proceso, Capacidad, Localización y Layout.',
    type: 'vf',
    chips: ['80 V/F', '7 temas'],
    dataFile: 'do1.json',
  },
  {
    slug: 'sibw',
    title: 'Sistemas de Información Basados en Web',
    code: 'Informática · SIBW',
    icon: '🌐',
    description: '178 preguntas tipo test sobre Introducción, Gestión de Información, Análisis/Diseño y Normativa.',
    type: 'test',
    chips: ['178 preguntas', '4 temas'],
    dataFile: 'sibw.json',
  },
  // ─── AÑADE AQUÍ NUEVAS ASIGNATURAS ───────────────
  // {
  //   slug: 'macroeconomia',
  //   title: 'Macroeconomía',
  //   code: 'Economía',
  //   icon: '📈',
  //   description: '...',
  //   type: 'vf',
  //   chips: ['XX preguntas'],
  //   dataFile: 'macro.json',
  // },
];
