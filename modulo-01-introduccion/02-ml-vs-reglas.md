# 1.2 ML vs. Sistemas Basados en Reglas

## El problema de las reglas

Considera un filtro de spam tradicional:

```python
# Sistema basado en reglas
if "gratis" in email and "urgente" in email:
    clasificar_como_spam()
elif longitud_email > 10000:
    clasificar_como_spam()
# ... cientos de reglas más
```

**Problemas de este enfoque:**

- Las reglas se vuelven inmanejables con el tiempo
- Los spammers adaptan sus mensajes para evadir las reglas
- Mantener el código es costoso y propenso a errores

## La solución con ML

En lugar de escribir reglas manualmente, dejamos que el modelo las descubra:

### Paso 1: Obtener datos

Recopilar ejemplos de emails etiquetados como spam y no-spam.

### Paso 2: Definir features

Convertir cada email en un conjunto de características numéricas:

- ¿Contiene palabras como "gratis", "oferta"?
- Longitud del email
- Cantidad de enlaces
- ¿El remitente está en la lista de contactos?

### Paso 3: Entrenar el modelo

El algoritmo de ML encuentra automáticamente los patrones que distinguen spam de no-spam.

## Comparación

| Aspecto | Reglas | ML |
|---------|--------|----|
| Mantenimiento | Complejo, manual | Se re-entrena con datos nuevos |
| Adaptabilidad | Baja (requiere código nuevo) | Alta (aprende de nuevos patrones) |
| Escalabilidad | Difícil | Natural |
| Transparencia | Alta (sabes las reglas) | Menor (depende del modelo) |

## ¿Cuándo usar cada uno?

- **Reglas**: cuando la lógica es simple, clara y no cambia
- **ML**: cuando los patrones son complejos, cambiantes o difíciles de codificar

---

**Anterior**: [¿Qué es ML?](01-que-es-ml.md) | **Siguiente**: [Aprendizaje Supervisado](03-aprendizaje-supervisado.md)
