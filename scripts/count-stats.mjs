#!/usr/bin/env node

/**
 * Script de cuantificación y métricas de contenido para repasaYA.
 *
 * Cuenta con precisión matemática el total de preguntas (test, vf, reveal),
 * fichas (flashcards, glosario), asignaturas y bloques de material.
 *
 * Uso:
 *   node scripts/count-stats.mjs
 *   node scripts/count-stats.mjs --detail
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const materialsDir = path.join(rootDir, 'src/content/materials');
const subjectsDir = path.join(rootDir, 'src/content/subjects');

function walk(dir) {
  let results = [];
  if (!fs.existsSync(dir)) return results;
  const list = fs.readdirSync(dir);
  for (const file of list) {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat && stat.isDirectory()) {
      results = results.concat(walk(fullPath));
    } else {
      results.push(fullPath);
    }
  }
  return results;
}

const materialFiles = walk(materialsDir).filter((f) => f.endsWith('.json'));
const subjectFiles = walk(subjectsDir).filter((f) => f.endsWith('.md'));

let totalTests = 0;
let totalVF = 0;
let totalReveal = 0;
let totalFlashcards = 0;
let totalGlosario = 0;
let totalPDFs = 0;
let totalGuias = 0;

const breakdownBySubject = {};

for (const filePath of materialFiles) {
  try {
    const raw = fs.readFileSync(filePath, 'utf8');
    const data = JSON.parse(raw);
    const subject = data.subject || 'desconocida';
    const type = data.type;
    const count = Array.isArray(data.items) ? data.items.length : 0;

    if (!breakdownBySubject[subject]) {
      breakdownBySubject[subject] = {
        test: 0,
        vf: 0,
        reveal: 0,
        flashcards: 0,
        glosario: 0,
        pdf: 0,
        guia: 0,
        totalQuestions: 0,
        totalCards: 0,
      };
    }

    const sub = breakdownBySubject[subject];

    switch (type) {
      case 'test':
        totalTests += count;
        sub.test += count;
        sub.totalQuestions += count;
        break;
      case 'vf':
        totalVF += count;
        sub.vf += count;
        sub.totalQuestions += count;
        break;
      case 'reveal':
        totalReveal += count;
        sub.reveal += count;
        sub.totalQuestions += count;
        break;
      case 'flashcards':
        totalFlashcards += count;
        sub.flashcards += count;
        sub.totalCards += count;
        break;
      case 'glosario':
        totalGlosario += count;
        sub.glosario += count;
        sub.totalCards += count;
        break;
      case 'apuntes':
      case 'examen':
        totalPDFs += 1;
        sub.pdf += 1;
        break;
      case 'guia':
        totalGuias += 1;
        sub.guia += 1;
        break;
    }
  } catch (err) {
    console.error(`Error procesando archivo ${filePath}:`, err.message);
  }
}

const totalQuestions = totalTests + totalVF + totalReveal;
const totalCards = totalFlashcards + totalGlosario;
const isDetail = process.argv.includes('--detail');

console.log('╔════════════════════════════════════════════════════════════╗');
console.log('║               repasaYA — Métricas de Contenido              ║');
console.log('╚════════════════════════════════════════════════════════════╝');
console.log(`📌 Total Preguntas Activas:   ${totalQuestions.toLocaleString('es-ES')}`);
console.log(`   ├─ Tipo Test:              ${totalTests.toLocaleString('es-ES')}`);
console.log(`   ├─ Verdadero / Falso:      ${totalVF.toLocaleString('es-ES')}`);
console.log(`   └─ Respuesta Oculta:       ${totalReveal.toLocaleString('es-ES')}`);
console.log(`📌 Total Fichas y Glosarios:  ${totalCards.toLocaleString('es-ES')}`);
console.log(`   ├─ Flashcards:             ${totalFlashcards.toLocaleString('es-ES')}`);
console.log(`   └─ Términos de Glosario:   ${totalGlosario.toLocaleString('es-ES')}`);
console.log(`📌 Total Documentos PDF:      ${totalPDFs}`);
console.log(`📌 Total Guías y Recursos:    ${totalGuias}`);
console.log(`📌 Total Asignaturas:         ${subjectFiles.length}`);
console.log(`📌 Bloques de Material:       ${materialFiles.length}`);
console.log('────────────────────────────────────────────────────────────');

if (isDetail) {
  console.log('\n📊 Desglose por Asignatura:');
  for (const [sub, data] of Object.entries(breakdownBySubject)) {
    console.log(` • ${sub}:`);
    if (data.totalQuestions > 0) {
      console.log(`     - Preguntas: ${data.totalQuestions} (test: ${data.test}, vf: ${data.vf}, rev: ${data.reveal})`);
    }
    if (data.totalCards > 0) {
      console.log(`     - Fichas: ${data.totalCards} (fc: ${data.flashcards}, glos: ${data.glosario})`);
    }
    if (data.pdf > 0) console.log(`     - PDFs: ${data.pdf}`);
    if (data.guia > 0) console.log(`     - Guías: ${data.guia}`);
  }
}
