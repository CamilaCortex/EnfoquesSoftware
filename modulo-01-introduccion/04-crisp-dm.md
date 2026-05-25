# 1.4 Metodología CRISP-DM

## ¿Qué es CRISP-DM?

**CRISP-DM** (Cross-Industry Standard Process for Data Mining) es la metodología estándar para proyectos de datos y ML. Define 6 fases iterativas que guían un proyecto desde la idea hasta producción.

## Las 6 fases

```text
┌─────────────────────────────────────────┐
│  1. Comprensión del negocio             │
│  2. Comprensión de los datos            │
│  3. Preparación de los datos            │
│  4. Modelado                            │
│  5. Evaluación                          │
│  6. Despliegue                          │
└─────────────────────────────────────────┘
         ↑                    │
         └────── iteración ───┘
```

### 1. Comprensión del negocio

- ¿Cuál es el problema que queremos resolver?
- ¿Realmente necesitamos ML o basta con reglas simples?
- ¿Cómo medimos el éxito? (KPI, métrica de negocio)

### 2. Comprensión de los datos

- ¿Qué datos tenemos disponibles?
- ¿Son suficientes? ¿Están completos?
- ¿Necesitamos fuentes adicionales?

### 3. Preparación de los datos

- Limpieza: valores faltantes, duplicados, ruido
- Transformación: convertir a formato tabular
- Feature engineering: crear variables nuevas útiles

### 4. Modelado

- Entrenar diferentes modelos
- Comparar resultados
- Si los resultados no son buenos → volver a paso 3

### 5. Evaluación

- ¿El modelo resuelve el problema de negocio?
- ¿La métrica es aceptable para producción?
- Pruebas con datos que el modelo no ha visto

### 6. Despliegue

- Llevar el modelo a producción (API, servicio web)
- Monitorear su rendimiento
- Planificar re-entrenamiento

## Principio clave: Iteración

Los proyectos de ML **no son lineales**. Se itera constantemente:

1. Empieza simple
2. Obtén feedback
3. Mejora

No busques la perfección en la primera iteración. Un modelo simple funcionando en producción vale más que un modelo perfecto que nunca se despliega.

---

**Anterior**: [Aprendizaje Supervisado](03-aprendizaje-supervisado.md) | **Siguiente**: [Selección de Modelos](05-seleccion-modelos.md)
