import fs from 'node:fs';
import path from 'node:path';
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

/* Materiales marcados `hidden` en la colección: generan página con
   noindex, pero tampoco deben aparecer en el sitemap. Se leen del disco
   para no tener que mantener la lista a mano. */
function hiddenSlugs() {
  const root = path.join(process.cwd(), 'src/content/materials');
  const found = new Set();
  const walk = (dir) => {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, e.name);
      if (e.isDirectory()) walk(full);
      else if (e.name.endsWith('.json')) {
        try {
          if (JSON.parse(fs.readFileSync(full, 'utf8')).hidden) {
            found.add(e.name.replace(/\.json$/, ''));
          }
        } catch {}
      }
    }
  };
  try {
    walk(root);
  } catch {}
  return found;
}

const HIDDEN = hiddenSlugs();

export default defineConfig({
  site: 'https://repasaya.juliancarrion.dev',
  base: '/',
  output: 'static',
  integrations: [sitemap({ filter: (page) => ![...HIDDEN].some((s) => page.endsWith(`/${s}/`)) })],

  /* Las rutas planas antiguas están indexadas desde hace meses. En estático
     Astro las convierte en páginas meta-refresh, que es lo máximo que
     permite GitHub Pages (no hay forma de devolver un 301 real). */
  redirects: {
    '/repasaYA': '/',
    '/rrhh': '/ade/4/c2/rrhh/',
    '/rrhh/quiz': '/ade/4/c2/rrhh/test/',
    '/rrhh/glosario': '/ade/4/c2/rrhh/glosario/',
    '/organizacion-empresas': '/ade/4/c2/organizacion-empresas/',
    '/organizacion-empresas/secreto': '/ade/4/c2/organizacion-empresas/secreto/',
    '/organizacion-empresas/quiz': '/ade/4/c2/organizacion-empresas/test/',
    '/organizacion-empresas/glosario': '/ade/4/c2/organizacion-empresas/flashcards/',
    '/do1': '/ade/4/c1/do1/',
    '/aef': '/ade/4/c2/aef/',
    '/aef/quiz': '/ade/4/c2/aef/test/',
    '/aef/glosario': '/ade/4/c2/aef/flashcards/',
    '/mp': '/informatica/1/c2/mp/',
    '/mp/quiz': '/informatica/1/c2/mp/test/',
    '/sibw': '/informatica/4/c2/sibw/',
    '/sibw/quiz': '/informatica/4/c2/sibw/test/',
    '/sibw/glosario': '/informatica/4/c2/sibw/flashcards/',
    '/dsd': '/informatica/4/c2/dsd/',
    '/dsd/vf': '/informatica/4/c2/dsd/vf/',
    '/dsd/apuntes': '/informatica/4/c2/dsd/apuntes-t4-t5/',
    '/scd': '/informatica/3/c1/sistemas-concurrentes-y-distribuidos/',
    '/scd/test': '/informatica/3/c1/sistemas-concurrentes-y-distribuidos/test/',
    '/scd/apuntes': '/informatica/3/c1/sistemas-concurrentes-y-distribuidos/apuntes/',
    '/scd/relaciones': '/informatica/3/c1/sistemas-concurrentes-y-distribuidos/relaciones/',
    '/informatica/3/c1/sistemas-concurrentes-y-distribuidos/guia': '/scd/guia/',
  },
});
