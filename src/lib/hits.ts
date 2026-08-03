/**
 * Contador de visitas de hits.sh.
 *
 * hits.sh solo publica un SVG: no tiene API JSON y no manda cabeceras CORS,
 * así que el navegador no puede pedir el número. Se lee aquí, en build, y se
 * pinta como una cifra más del hero con la tipografía del sitio — meter su
 * SVG en la fila desentonaría, porque trae su propia fuente.
 *
 * Contrapartida: el número es el del último despliegue, no el de este
 * segundo. Quien suma las visitas es el píxel de `VisitCounter.astro`, que
 * sí pide el SVG desde el navegador.
 *
 * La clave (`jxliian.github.io/repasaYA`) es la histórica: cambiarla
 * reiniciaría la cuenta desde cero.
 */

export const HITS_KEY = 'jxliian.github.io/repasaYA';
export const HITS_SVG = `https://hits.sh/${HITS_KEY}.svg?style=flat-square&label=&color=a78bea&labelColor=a78bea`;

/**
 * Devuelve el total de visitas ya formateado, o `null` si hits.sh no
 * responde. Un contador caído nunca debe tumbar el build: quien llama
 * simplemente omite la cifra.
 */
export async function fetchHits(): Promise<string | null> {
  try {
    const res = await fetch(`https://hits.sh/${HITS_KEY}.svg`, {
      signal: AbortSignal.timeout(6000),
    });
    if (!res.ok) return null;

    const svg = await res.text();
    // El SVG repite el número en dos <text> (sombra y relieve): vale el último
    const matches = [...svg.matchAll(/>([\d.,]+[kKmM]?)<\/text>/g)];
    const raw = matches.at(-1)?.[1];
    if (!raw) return null;

    // "1,159" → 1159 → "1.159" (separador español). Si viene abreviado
    // ("12.3k"), se deja tal cual.
    if (/^[\d,]+$/.test(raw)) {
      const n = parseInt(raw.replace(/,/g, ''), 10);
      if (!Number.isFinite(n)) return null;
      return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    }
    return raw;
  } catch {
    return null;
  }
}
