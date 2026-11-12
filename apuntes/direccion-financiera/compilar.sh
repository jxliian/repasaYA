#!/usr/bin/env bash
# Compila los PDFs de Dirección Financiera y los publica en public/
#   apuntes_dfin.tex  -> apuntes-primer-parcial.pdf
#   relacion_dfin.tex -> relacion-problemas-resueltos.pdf
set -e
cd "$(dirname "$0")"
DEST=../../public/ade/direccion-financiera
build() {
  pdflatex -interaction=nonstopmode -halt-on-error "$1.tex" >/dev/null
  pdflatex -interaction=nonstopmode -halt-on-error "$1.tex" >/dev/null
  echo "$1: Overfull $(grep -c "Overfull" "$1.log" || true) · páginas $(pdfinfo "$1.pdf" 2>/dev/null | awk '/^Pages/{print $2}')"
  cp "$1.pdf" "$DEST/$2"
}
build apuntes_dfin apuntes-primer-parcial.pdf
build relacion_dfin relacion-problemas-resueltos.pdf
