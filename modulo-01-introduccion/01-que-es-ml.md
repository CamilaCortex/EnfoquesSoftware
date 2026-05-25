# 1.1 ¿Qué es Machine Learning?

## Idea Central

Machine Learning (ML) es el proceso de **extraer patrones a partir de datos** para hacer predicciones sobre datos nuevos.

## Ejemplo: Predecir el precio de un auto

Imagina que quieres predecir el precio de un auto usado. Tienes datos históricos con información como:

- Año del modelo
- Kilometraje
- Marca
- Tipo de combustible

Estos son los **features** (características). El precio es el **target** (variable objetivo).

```
Datos históricos          →  Modelo aprende patrones
Datos nuevos (sin precio) →  Modelo predice el precio
```

## Definición formal

ML tiene dos componentes principales:

- **Features (X)**: información que describe cada observación
- **Target (y)**: lo que queremos predecir

El modelo aprende la relación entre X e y durante el **entrenamiento**, y luego usa esa relación para predecir y en datos nuevos.

## ¿Por qué es útil?

- Automatiza decisiones que serían muy complejas de programar manualmente
- Mejora con más datos (a diferencia de reglas fijas)
- Se aplica en muchos dominios: finanzas, salud, comercio, etc.

---

**Siguiente**: [ML vs. Sistemas Basados en Reglas](02-ml-vs-reglas.md)
