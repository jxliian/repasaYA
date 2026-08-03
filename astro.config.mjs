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
  site: 'https://jxliian.github.io',
  base: '/repasaYA',
  output: 'static',
  integrations: [sitemap({ filter: (page) => ![...HIDDEN].some((s) => page.endsWith(`/${s}/`)) })],

  /* Las rutas planas antiguas están indexadas desde hace meses. En estático
     Astro las convierte en páginas meta-refresh, que es lo máximo que
     permite GitHub Pages (no hay forma de devolver un 301 real).

     OJO: la clave va relativa al `base`, pero el destino NO — Astro lo
     escribe literal en el meta refresh, así que hay que incluir /repasaYA. */
  redirects: {
    '/rrhh': '/repasaYA/ade/4/c2/rrhh/',
    '/rrhh/quiz': '/repasaYA/ade/4/c2/rrhh/test/',
    '/rrhh/glosario': '/repasaYA/ade/4/c2/rrhh/glosario/',
    '/organizacion-empresas': '/repasaYA/ade/4/c2/organizacion-empresas/',
    '/organizacion-empresas/secreto': '/repasaYA/ade/4/c2/organizacion-empresas/secreto/',
    '/organizacion-empresas/quiz': '/repasaYA/ade/4/c2/organizacion-empresas/test/',
    '/organizacion-empresas/glosario': '/repasaYA/ade/4/c2/organizacion-empresas/flashcards/',
    '/do1': '/repasaYA/ade/4/c1/do1/',
    '/aef': '/repasaYA/ade/4/c2/aef/',
    '/aef/quiz': '/repasaYA/ade/4/c2/aef/test/',
    '/aef/glosario': '/repasaYA/ade/4/c2/aef/flashcards/',
    '/mp': '/repasaYA/informatica/1/c2/mp/',
    '/mp/quiz': '/repasaYA/informatica/1/c2/mp/test/',
    '/sibw': '/repasaYA/informatica/4/c2/sibw/',
    '/sibw/quiz': '/repasaYA/informatica/4/c2/sibw/test/',
    '/sibw/glosario': '/repasaYA/informatica/4/c2/sibw/flashcards/',
    '/dsd': '/repasaYA/informatica/4/c2/dsd/',
    '/dsd/vf': '/repasaYA/informatica/4/c2/dsd/vf/',
    '/dsd/apuntes': '/repasaYA/informatica/4/c2/dsd/apuntes-t4-t5/',
  },
});
