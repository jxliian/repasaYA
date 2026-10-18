#!/usr/bin/env bash
# Script para compilar el proyecto LaTeX de FFT (Fundamentos Físicos y Tecnológicos)
cd "$(dirname "$0")" || exit 1

echo "==> Compilando apuntes de FFT con pdflatex..."
pdflatex -interaction=nonstopmode main.tex > /dev/null
pdflatex -interaction=nonstopmode main.tex

if [ $? -eq 0 ]; then
    cp main.pdf apuntes_fft.pdf
    echo "==> [OK] Compilación exitosa: main.pdf y apuntes_fft.pdf generados correctamente."
else
    echo "==> [ERROR] Ocurrió un error en la compilación. Revisa main.log."
    exit 1
fi
