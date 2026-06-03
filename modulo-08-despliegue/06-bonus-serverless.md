# BONUS: Serverless (Funciones sin Servidor)

> Esta lección es material extra. No es obligatoria para el curso.

---

## ¿Qué es Serverless?

En lugar de mantener un servidor corriendo 24/7 (como nuestro Docker), con serverless solo se ejecuta código **cuando llega una petición**. No pagas por tiempo inactivo.

```text
Docker/FastAPI (siempre encendido):
  Servidor ████████████████████████ (24h corriendo)

Serverless (bajo demanda):
  ░░░░█░░░░░░█░░█░░░░░░░░░░░░█░░ (solo cuando hay peticiones)
```

## ¿Cuándo tiene sentido?

- Tráfico **bajo o esporádico** (pocas peticiones por hora)
- Quieres **cero mantenimiento** de infraestructura
- El modelo es **ligero** (carga rápida)

## ¿Cuándo NO conviene?

- Tráfico alto y constante (más caro que un servidor)
- Modelo pesado (el "cold start" hace la primera petición lenta)
- Necesitas mantener estado entre peticiones

## Proveedores populares

| Servicio | Proveedor | Nivel gratuito |
|----------|-----------|----------------|
| AWS Lambda | Amazon | Sí (1M peticiones/mes) |
| Cloud Functions | Google | Sí (2M peticiones/mes) |
| Azure Functions | Microsoft | Sí (1M peticiones/mes) |
| Modal | Modal Labs | Sí (limitado) |

## Ejemplo conceptual (pseudo-código)

```python
# En serverless, tu código se ve similar pero sin servidor explícito

def handler(event, context):
    """Esta función se ejecuta cuando llega una petición."""
    # Cargar modelo (idealmente cacheado)
    modelo = cargar_modelo()
    
    # Obtener datos del evento
    cliente = event['body']
    
    # Predecir
    resultado = modelo.predict(cliente)
    
    # Devolver respuesta
    return {
        'statusCode': 200,
        'body': {'churn_probability': resultado}
    }
```

## Diferencia con Docker

| Aspecto | Docker + FastAPI | Serverless |
|---------|-----------------|------------|
| Costo con poco tráfico | Fijo (servidor siempre on) | Muy bajo / gratis |
| Costo con mucho tráfico | Fijo (predecible) | Puede ser caro |
| Cold start | No (siempre listo) | Sí (primera petición lenta) |
| Control | Total | Limitado |
| Complejidad | Media | Baja |
| Escalabilidad | Manual (más réplicas) | Automática |

## Conclusión

Para este curso usamos Docker + FastAPI porque es el enfoque más profesional y estándar. Serverless es una alternativa válida para proyectos pequeños o prototipos rápidos.

---

**Volver al módulo**: [README](README.md)
