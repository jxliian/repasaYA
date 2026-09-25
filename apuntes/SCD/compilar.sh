#!/usr/bin/env bash
# Script para compilar el proyecto LaTeX de SCD
cd "$(dirname "$0")" || exit 1

echo "==> Compilando apuntes de SCD con pdflatex..."
pdflatex -interaction=nonstopmode main.tex > /dev/null
pdflatex -interaction=nonstopmode main.tex

if [ $? -eq 0 ]; then
    echo "==> [OK] Compilación exitosa: main.pdf generado correctamente."
else
    echo "==> [ERROR] Ocurrió un error en la compilación. Revisa main.log."
    exit 1
fi
