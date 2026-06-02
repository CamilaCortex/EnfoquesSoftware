# Guía de Métricas de Clasificación

---

## 1. La Matriz de Confusión

### ¿Qué es?

Es una tabla que muestra cuántas veces el modelo acertó y en qué se equivocó.

```
              PREDICHO
           Positivo  Negativo
REAL Pos  |   TP   |   FN   |
     Neg  |   FP   |   TN   |
```

### Los 4 valores clave

| Valor | Nombre | Significado |
|-------|--------|-------------|
| **TP** | Verdadero Positivo | Era positivo y predijo positivo ✅ |
| **TN** | Verdadero Negativo | Era negativo y predijo negativo ✅ |
| **FP** | Falso Positivo | Era negativo pero predijo positivo ❌ |
| **FN** | Falso Negativo | Era positivo pero predijo negativo ❌ |

### Ejemplo: Detector de Spam

```
              PREDICHO
           Spam  Normal
REAL Spam |  45 |   5  |   → De 50 spams reales: 45 detectados, 5 perdidos
     Normal|  3  |  97  |   → De 100 normales: 97 correctos, 3 alarmas falsas
```

---

## 2. Accuracy (Exactitud)

### ¿Qué mide?
De todas las predicciones, ¿cuántas acertó el modelo?

### Fórmula
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

### Ejemplo
```
Accuracy = (45 + 97) / (45 + 97 + 3 + 5) = 142 / 150 = 94.6%
```

### ⚠️ Trampa del Accuracy en Datasets Desbalanceados

Imagina detección de fraude bancario:
- 99 transacciones normales
- 1 transacción fraudulenta

Un modelo que **siempre predice "no fraude"**:
```
Accuracy = 99 / 100 = 99%  ← Parece excelente
```

**¡Pero no detectó ni un solo fraude!**

> Regla de oro: Si tus clases están desbalanceadas, **nunca confíes solo en Accuracy**.

---

## 3. Precision (Precisión)

### ¿Qué mide?
De todo lo que el modelo predijo como positivo, ¿cuántos eran realmente positivos?

```
Precision = TP / (TP + FP)
```

### Cuándo usarla
Cuando los **falsos positivos son costosos**.

**Ejemplo:** Filtro de spam
- Un FP = email importante clasificado como spam
- Mejor ser conservador y dejar pasar algo de spam que perder emails importantes

```
Precision = 45 / (45 + 3) = 93.75%
```

---

## 4. Recall (Sensibilidad)

### ¿Qué mide?
De todos los casos positivos reales, ¿cuántos detectó el modelo?

```
Recall = TP / (TP + FN)
```

### Cuándo usarlo
Cuando los **falsos negativos son costosos**.

**Ejemplo:** Detección de cáncer
- Un FN = cáncer no detectado (puede costar una vida)
- Mejor dar una falsa alarma que perder un caso real

```
Recall = 45 / (45 + 5) = 90%
```

---

## 5. F1-Score

### ¿Qué mide?
Es el balance entre Precision y Recall en un solo número.

```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

### Cuándo usarlo
Cuando necesitas balance entre Precision y Recall, especialmente con clases desbalanceadas.

```
F1 = 2 × (0.9375 × 0.90) / (0.9375 + 0.90) = 0.9184 = 91.84%
```

---

## 6. Variantes del F1-Score en Multiclase

### El Problema
En clasificación multiclase (ej: 3 clases), necesitas agregar el F1 de cada clase en un solo número. Hay 3 formas de hacerlo.

---

### F1-Macro

**Trata todas las clases por igual, sin importar su tamaño.**

```
Paso 1: Calcular F1 para cada clase
  F1_Clase_A = 0.90
  F1_Clase_B = 0.80
  F1_Clase_C = 0.70

Paso 2: Promediar
  F1-Macro = (0.90 + 0.80 + 0.70) / 3 = 0.80
```

**Cuándo usarlo:** Cuando todas las clases son igualmente importantes.

**Ejemplo real:** Sistema de triage médico donde cada nivel de urgencia es igual de crítico.

---

### F1-Micro

**Agrega todos los TP, FP, FN globalmente antes de calcular.**

```
Paso 1: Sumar todos los TP, FP, FN
  TP_global = TP_A + TP_B + TP_C
  FP_global = FP_A + FP_B + FP_C
  FN_global = FN_A + FN_B + FN_C

Paso 2: Calcular F1 global
  F1-Micro = 2 × TP_global / (2 × TP_global + FP_global + FN_global)
```

**Cuándo usarlo:** Cuando el volumen importa y las clases grandes deben pesar más.

> En clasificación multiclase, F1-Micro es equivalente al Accuracy.

---

### F1-Weighted

**Promedia el F1 de cada clase ponderado por su tamaño.**

```
Paso 1: Calcular F1 por clase y contar muestras
  F1_A = 0.90, n_A = 500
  F1_B = 0.70, n_B = 300
  F1_C = 0.50, n_C = 200
  Total = 1000

Paso 2: Ponderar por tamaño
  F1-Weighted = (0.90×500 + 0.70×300 + 0.50×200) / 1000
              = (450 + 210 + 100) / 1000
              = 0.76
```

**Cuándo usarlo:** Cuando el volumen de cada clase refleja su importancia en el negocio.

**Ejemplo real:** E-commerce donde Electrónica (70% ventas) importa más que Libros (5% ventas).

---

### Comparación de las 3 Variantes

| Variante | Trata clases | Cuándo usar |
|----------|-------------|-------------|
| **Macro** | Por igual | Todas las clases son igual de importantes |
| **Micro** | Por volumen global | El rendimiento general importa más |
| **Weighted** | Por tamaño de clase | El volumen refleja importancia del negocio |

---

## 7. Matriz de Confusión Multiclase

### Ejemplo con Iris (3 clases)

```
                    PREDICHO
                 Setosa  Versicolor  Virginica
REAL  Setosa   |  50   |     0     |    0    |
      Versicolor|   0   |    45     |    5    |
      Virginica |   0   |     3     |   47    |
```

### Cómo leerla

> **Filas = Lo que ERA realmente**
> **Columnas = Lo que el modelo PREDIJO**

```
Fila Versicolor → De 50 Versicolors reales:
                  45 predijo bien ✅
                   5 confundió con Virginica ❌
```

### Las 3 Reglas de Oro

1. **Diagonal = Aciertos** → Todo lo que el modelo acertó
2. **Fuera de diagonal = Errores** → Confusión entre clases
3. **Suma de fila = Total real** de esa clase

### TP, FP, FN para UNA Clase (One-vs-Rest)

**Enfocados en Versicolor:**

```
TP = 45   → Diagonal de Versicolor (acertó)
FN = 5    → Fila Versicolor, fuera diagonal (era Versicolor pero falló)
FP = 3    → Columna Versicolor, fuera diagonal (no era pero predijo Versicolor)
```

```
Regla fácil:
TP → Diagonal de la clase
FN → Resto de la FILA       (el modelo la confundió con otras)
FP → Resto de la COLUMNA    (el modelo confundió otras con esta)
```

---

## 8. Curva ROC y AUC

### El Problema de Partida

Un modelo no dice directamente "spam" o "no spam", sino que da una **probabilidad**:

```
Email A → 0.95  (muy probablemente spam)
Email B → 0.60  (tal vez spam)
Email C → 0.10  (probablemente no spam)
```

**¿A partir de qué probabilidad dices "ES SPAM"?** → Eso es el umbral.

---

### ¿Qué es la Curva ROC?

Una gráfica que muestra el trade-off entre detectar bien los positivos y no generar falsas alarmas, al mover el umbral de decisión.

**Los dos ejes:**

```
Eje Y = TPR (Recall/Sensibilidad)
      = TP / (TP + FN)
      = "¿Qué % de spam real detecté?"

Eje X = FPR (Tasa de Falsos Positivos)
      = FP / (FP + TN)
      = "¿Qué % de emails normales clasifiqué mal como spam?"
```

### Cómo se Construye

Al mover el umbral de 1.0 a 0.0, cada punto es una posición en la gráfica:

```
Umbral 1.0 → Nada es spam      → TPR=0%,   FPR=0%   → Punto (0, 0)
Umbral 0.5 → Algo es spam      → TPR=70%,  FPR=20%  → Punto (0.2, 0.7)
Umbral 0.0 → Todo es spam      → TPR=100%, FPR=100% → Punto (1, 1)
```

Uniendo esos puntos → **Curva ROC**

---

### Los 3 Casos Clave

**Modelo Perfecto (AUC = 1.0)**
```
TPR 1.0 | ┌──────────
         | │
         | │
     0.0 | └──────────
           0.0       1.0  FPR
```

**Modelo Aleatorio (AUC = 0.5)**
```
TPR 1.0 |          /
         |        /
         |      /    ← Diagonal
         |    /
     0.0 |  /________
           0.0       1.0  FPR
```

**Modelo Bueno (AUC entre 0.7 y 0.99)**
```
TPR 1.0 |      ______
         |    _/
         |  _/
         | /
     0.0 |/___________
           0.0       1.0  FPR
```

---

### ¿Qué es el AUC?

> El **área bajo la curva ROC**, resumida en un número entre 0.5 y 1.0.

**Interpretación probabilística:**
> AUC = probabilidad de que el modelo le dé una puntuación más alta a un caso positivo elegido al azar que a un caso negativo elegido al azar.

### Escala de Valores

| AUC | Interpretación |
|-----|----------------|
| **1.0** | Modelo perfecto |
| **0.9 - 1.0** | Excelente |
| **0.8 - 0.9** | Bueno |
| **0.7 - 0.8** | Aceptable |
| **0.6 - 0.7** | Pobre |
| **0.5** | Aleatorio (inútil) |
| **< 0.5** | Peor que el azar |

---

### ROC vs Curva Precision-Recall

| Situación | Usar |
|-----------|------|
| Clases balanceadas | **ROC-AUC** |
| Clases desbalanceadas | **Precision-Recall** |
| Comparar modelos en general | **ROC-AUC** |
| Optimizar clase minoritaria | **Precision-Recall** |

---

## 9. Resumen General

### ¿Qué métrica usar según el caso?

| Caso | Métrica Recomendada |
|------|-------------------|
| Clases balanceadas | Accuracy + F1 |
| Clases desbalanceadas | Precision + Recall + F1 |
| Detectar todos los positivos (cáncer) | **Recall** |
| Evitar falsas alarmas (spam) | **Precision** |
| Balance general | **F1-Score** |
| Comparar modelos | **AUC-ROC** |
| Todas las clases igual de importantes | **F1-Macro** |
| Volumen refleja importancia | **F1-Weighted** |

### Reglas de Oro

> 1. **Nunca confíes solo en Accuracy** con datos desbalanceados.
> 2. **Recall** cuando un FN es muy costoso (medicina, fraude).
> 3. **Precision** cuando un FP es muy costoso (spam, diagnóstico).
> 4. **F1-Macro** cuando todas las clases son igual de críticas.
> 5. **AUC-ROC** para comparar modelos de forma general.
