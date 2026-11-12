#!/usr/bin/env bash
# Compila los apuntes de Dirección Financiera y publica el PDF en public/
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode -halt-on-error apuntes_dfin.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error apuntes_dfin.tex >/dev/null
echo "Overfull: $(grep -c "Overfull" apuntes_dfin.log || true)"
cp apuntes_dfin.pdf ../../public/ade/direccion-financiera/apuntes-primer-parcial.pdf
