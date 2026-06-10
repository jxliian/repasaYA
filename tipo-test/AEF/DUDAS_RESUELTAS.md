# DUDAS RESUELTAS — AEF

---

## 1. ¿El PMM depende del tipo de empresa?

**Sí.** La composición del período medio de maduración varía según el tipo de empresa:

| Tipo | Fórmula PMM |
|------|-------------|
| **Comercial** | SV + SC |
| **Industrial** | SA + SF + SV + SC |
| **Mixta** | SA + SF + SV(combinado) + SC |

- **SA** = subperiodo almacenamiento materias primas
- **SF** = subperiodo fabricación
- **SV** = subperiodo venta / almacenamiento productos terminados
- **SC** = subperiodo cobro a clientes

> **Clave:** Una empresa industrial SIEMPRE incluye el SF (fabricación). Si no te lo dan en la tabla de indicadores, puede ser 0 o estar integrado en otro subperiodo, pero no lo ignores por defecto.

**PMMF** = PMM − Subperiodo pago a proveedores

---

## 2. ¿Qué es el coste de producción terminada?

Es el coste total de los productos que han **salido del proceso productivo** y están listos para venderse. Fórmula:

```
Coste producción terminada =
  Consumo de materias primas
  + Mano de obra directa
  + Amortizaciones de producción
  + Otros gastos de fabricación
  − Variación de productos en curso (Δ existencias en curso)
```

- Si aumentan los productos en curso → se resta (parte del coste queda "atrapada" en proceso)
- Si disminuyen los productos en curso → se suma (se añade al coste de lo terminado)

---

## 3. ¿Qué es el resultado financiero?

```
Resultado financiero = Ingresos financieros − Gastos financieros
```

- **Ingresos financieros**: dividendos recibidos, intereses de préstamos concedidos, rendimientos de inversiones financieras
- **Gastos financieros**: intereses de deudas, comisiones bancarias

> Si es **negativo** → la empresa paga más intereses de los que cobra (empresa endeudada).
> Si es **positivo** → la empresa tiene más inversiones financieras que deuda (poco habitual en industriales).

En el PyG funcional:
```
RNEX → + Resultado financiero → RAI → − Impuesto → Resultado del ejercicio
```

---

## 4. ¿Qué miro cuando hablan de "financiación que obtiene la empresa"?

Miras el **pasivo y el patrimonio neto** (el lado derecho del balance), NO el activo.

| Tipo de financiación | Dónde está |
|----------------------|------------|
| Financiación **propia** | Patrimonio Neto (PN): capital, reservas, resultado del ejercicio |
| Financiación **ajena a l/p** | Pasivo No Corriente (PNC): deudas l/p, obligaciones |
| Financiación **ajena a c/p** | Pasivo Corriente (PC): deudas c/p, proveedores, acreedores |

**En términos netos** → miras la **variación** de cada partida entre los dos ejercicios:
- Si PN sube → financiación propia nueva (resultado retenido, ampliación capital)
- Si PNC sube → financiación ajena nueva a l/p
- Si PC sube → financiación ajena nueva a c/p

> El **activo** te dice en qué se ha INVERTIDO esa financiación, no de dónde viene.

---

## 5. Diferencia entre variaciones del RNEX y del resultado del ejercicio

**¿Por qué el resultado del ejercicio puede caer menos % que el RNEX, o al revés?**

Porque parten de **bases diferentes** y entre uno y otro hay más partidas:

```
RNEX
  + Resultado financiero
  = RAI
  − Impuesto sobre beneficios
  = Resultado del ejercicio
```

**Ejemplo Dulcesol 2023:** RNEX −147,87% pero resultado del ejercicio solo −40,48%.

Motivos por los que divergen:
1. **Base distinta**: el mismo deterioro absoluto en euros representa % diferente si la base es más pequeña
2. **Resultado financiero**: si los ingresos financieros suben o los gastos financieros bajan, amortiguan la caída del RNEX
3. **Resultado atípico**: un ingreso extraordinario (enajenaciones, subvenciones) puede compensar parcialmente
4. **Efecto fiscal**: si el RAI baja, el impuesto también baja, lo que protege parcialmente el resultado final

> **Trampa de examen**: FGO = Resultado del ejercicio + Amortizaciones (NO es RNEX + Amortizaciones)

---

## 6. FGO vs FGO antes de intereses e impuestos — ¿cuál es cuál?

| Concepto | Fórmula |
|----------|---------|
| **FGO** | Resultado del ejercicio + Amortizaciones |
| **FGO antes de intereses e impuestos** | RNEX + Amortizaciones |

La diferencia: el FGO "normal" ya tiene descontados gastos financieros e impuestos. El "antes de intereses e impuestos" (también llamado FEAE aproximado) parte del RNEX.

> En el PyG funcional el FGO se calcula como: RBGE + Ingresos financieros − Gastos financieros − Impuesto (equivale a Resultado + Amortizaciones).

---

## 7. ¿Cuáles son los activos ajenos a la explotación?

Son activos que **no participan en la actividad principal** de la empresa:

| Activo ajeno | Dónde aparece |
|--------------|---------------|
| Inversiones financieras **l/p** (participaciones en otras empresas, préstamos l/p) | ANC |
| Inversiones financieras **c/p** (depósitos, valores negociables c/p) | AC |

**Por qué importa:**

```
RE de explotación = RNEX / Activo de explotación
                              ↑
           Activo Total − Inversiones financieras
```

```
RE global = (RAI + GF) / Activo Total
                              ↑
                  Incluye TODO (también las inv. financieras)
```

> Ejemplo INDESPA: Activo Total = 32.500 | Inv. financieras l/p = 4.800 → **Activo explotación = 27.700**

---

## 8. ¿En el examen ordinario me dan los subperiodos o los calculo?

**Te los dan** en la tabla de indicadores. No tienes que calcularlos.

- En el **parcial** (ejercicio práctico) sí los calculas desde el balance y PyG.
- En la **ordinaria**, la tabla de indicadores ya viene con todos los subperiodos calculados. Solo los interpretas o los usas para calcular PMM y PMMF.

---

## 9. ¿Por qué FM/NOF/RLN → "capitales permanentes"? (INDESPA 2021)

Datos: FM = 315.153 | NOF = 262.622 | RLN = 52.531

Lógica:

```
RLN = FM − NOF = 315.153 − 262.622 = 52.531 > 0
```

| Resultado | Interpretación |
|-----------|---------------|
| RLN > 0 | El FM es MAYOR que las NOF → los capitales permanentes financian las NOF y sobra liquidez |
| RLN < 0 | El FM no llega a cubrir las NOF → hay que recurrir a deuda financiera a c/p |
| NOF < 0 | Los proveedores financian el ciclo y generan excedente (ej. Mercadona) |

> **Capitales permanentes** = Fondos Propios + Pasivo No Corriente (financiación estable). Cuando RLN > 0, son ellos quienes cubren las NOF.

---

## 10. ¿Por qué la eficiencia del personal sube si el ratio valor añadido/gasto personal pasa de 2,93 a 3,85? (INDESPA)

```
Eficiencia personal = Valor añadido / Gasto de personal
```

- 2020: 2,93 → por cada €1 de gasto en personal, se generan 2,93€ de valor añadido
- 2021: 3,85 → por cada €1 de gasto en personal, se generan 3,85€ de valor añadido

Como el ratio **sube**, cada euro gastado en personal genera **más valor** → la eficiencia **mejora**.

> Las trampas: el gasto medio por empleado subió (3.297 → 3.338€) y el nº de empleados bajó (49,5 → 42,5). Pero el ratio que mide eficiencia es el de valor añadido/gasto, y ese sí mejoró. → **Respuesta c)**

---

## 11. ¿Por qué Viscofan subperiodos → d) todas correctas?

Datos 2023: SA=68d | SF=27d | SV=? | Subperiodo pago proveedores=82d | SA+SF+SV (proceso producción y venta)=167d

Las tres afirmaciones:
- a) "Algo más de dos meses en renovar almacén MP" → 68 días ≈ 2,3 meses ✓
- b) "Algo menos de un mes en producir" → SF=27 días < 30 días ✓
- c) "Tarda menos en pagar a proveedores (82d) que en realizar proceso producción y venta (167d)" → 82 < 167 ✓

Todas son correctas → **d)**

> La clave de c): "proceso productivo y de venta" = SA+SF+SV = 167 días (no solo SF=27 días). El subperiodo de pago (82d) es menor que los 167d del proceso completo.

---

## 12. ¿Qué recomendar para aumentar la RE total? (INDESPA) → d) todas correctas

```
RE total = (RAI + GF) / Activo Total = Margen × Rotación
```

Para aumentarla puedes actuar sobre:
- **a) Reducir consumos** → sube el margen (RNEX/Ventas) → sube RE ✓
- **b) Aumentar rotación de activos** → más ventas por cada € invertido → sube RE ✓
- **c) Aumentar rendimiento de inversiones financieras** → sube ingresos financieros → sube RAI → sube numerador de RE global ✓

Las tres vías son válidas → **d) Todas correctas**

---

## 13. ¿Por qué Al-Sur (RF=6%, RE=8%, Kd=4%) → d) b) y c) son correctas?

**b) Apalancamiento positivo:**
```
RE global (8%) > Kd (4%)
→ Efecto apalancamiento = (D/FP) × (8% − 4%) > 0 → POSITIVO ✓
```

**c) Grado de endeudamiento < 1 necesariamente:**

Formula: `RF = [RE + (D/FP) × (RE − Kd)] × (1 − t) = 6%`

Para que D/FP fuera ≥ 1:
```
RF_antes_imptos = 8% + (1 × 4%) = 12%
RF_neta = 12% × (1 − t) = 6% → t = 50%
```

Un tipo impositivo del 50% es irreal (España: 25%). Para cualquier t realista, D/FP < 1.

| t = 25% | D/FP = 0,00 | < 1 ✓ |
|---------|-------------|-------|
| t = 30% | D/FP = 0,14 | < 1 ✓ |
| t = 40% | D/FP = 0,50 | < 1 ✓ |
| t = 50% | D/FP = 1,00 | límite |

→ **d) b) y c) son correctas**

> Trampa: aunque RF (6%) < RE (8%), el apalancamiento SIGUE siendo positivo. La diferencia la causan los impuestos, no la estructura de deuda.

---

## 14. INDESPA vs competidora: ¿por qué INDESPA tiene RF mayor?

Datos:

|  | INDESPA | Competidora |
|--|---------|-------------|
| RE explotación | 22% | 25% |
| RE global | 18% | 14% |
| Ef. apalancamiento | 5% | 5% |
| Tasa impositiva | 25% | 25% |

```
RF = (RE global + Efecto apalancamiento) × (1 − t)

INDESPA:     (18% + 5%) × 0,75 = 17,25%
Competidora: (14% + 5%) × 0,75 = 14,25%
```

INDESPA tiene **RF mayor** (17,25% > 14,25%) aunque su RE de explotación sea menor.

> Clave: la RE global de INDESPA (18%) es mayor que la de la competidora (14%). Eso es lo que determina la RF, no la RE de explotación.

---

## 15. Sustituir financiación propia por ajena: ¿qué pasa con la RF?

```
RF_ai = RE global + (D/FP) × (RE global − Kd)
```

Si aumenta la deuda (D sube, FP baja → D/FP sube):

- Si **RE global > Kd** → (RE − Kd) > 0 → cada euro adicional de deuda **aumenta** la RF ✓
- Si **RE global < Kd** → (RE − Kd) < 0 → cada euro adicional de deuda **reduce** la RF

> Respuesta correcta: "Aumento de RF antes de impuestos **siempre que RE > coste de la financiación no propia**"
> La RE global NO cambia al cambiar la estructura financiera (el RNEX y el activo no varían por ello).

---

## 16. ¿Cómo se interpreta que el grado de composición del endeudamiento (PNC/PC) disminuya?

```
Composición endeudamiento = PNC / PC
```

Si el ratio **baja**: el numerador (deuda l/p) cae respecto al denominador (deuda c/p).
→ **Se ha reducido la proporción de deuda a largo plazo respecto al pasivo corriente.**

> No confundir: el ratio mide PNC **respecto a PC**, no respecto al pasivo total. Si baja, la deuda l/p pierde peso frente a la deuda c/p → estructura financiera más arriesgada (más deuda a c/p).

---

## 17. Cambio de vida útil del inmovilizado: ¿qué pasa con el FGO?

Si se **reduce la vida útil** (de 10 a 8 años) → la amortización anual **aumenta**.

Efecto:
- Resultado del ejercicio **baja** (más gasto de amortización)
- FGO = Resultado + Amortizaciones → el aumento de amortizaciones compensa con creces la caída del resultado:

```
ΔFGO = ΔAmortización × t > 0
```

→ **El FGO AUMENTA** aunque el resultado caiga, porque la amortización es un ajuste no monetario (no supone salida de caja).

---

## 18. EFE: ¿qué significa cada bloque?

Del EFE de INDESPA 2020:

- **A) Flujos de explotación positivos** → la empresa genera dinero con su actividad principal ✓
- **Variación capital corriente = +23.064€** → el capital corriente (AC − PC) aumentó ese año ✓
- **Variación neta de efectivo = −3.964€** → la tesorería bajó 3.964€ (los pagos superaron a los cobros)

> "Los cobros superan a los pagos en 3.964€" es **FALSO** — es al revés. Los pagos superan a los cobros.
