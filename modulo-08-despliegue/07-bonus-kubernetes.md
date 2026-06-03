# BONUS: Kubernetes (Orquestación de Contenedores)

> Esta lección es material extra. No es obligatoria para el curso.

---

## ¿Qué es Kubernetes?

Kubernetes (K8s) es un sistema para **gestionar múltiples contenedores Docker** en producción. Resuelve el problema de: "tengo mi contenedor funcionando, pero ¿qué pasa cuando tengo miles de usuarios?"

## ¿Qué problemas resuelve?

```text
Sin Kubernetes:
  1 contenedor → se cae → servicio muerto 💀

Con Kubernetes:
  3 contenedores → se cae 1 → K8s levanta otro automáticamente ✓
  Mucho tráfico → K8s crea más contenedores automáticamente ✓
```

## Conceptos básicos (solo vocabulario)

- **Pod**: la unidad mínima. Generalmente = 1 contenedor
- **Deployment**: define cuántas réplicas (pods) quieres
- **Service**: expone los pods al exterior (como un balanceador de carga)
- **Cluster**: el conjunto de máquinas donde corren los pods

## Ejemplo visual

```text
                    Internet
                       │
                   [Service]
                   /    |    \
              [Pod 1] [Pod 2] [Pod 3]
               (tu     (tu     (tu
              Docker)  Docker)  Docker)
```

Si un pod se cae, Kubernetes lo reemplaza automáticamente.

## ¿Cuándo necesitas Kubernetes?

- **Miles o millones** de peticiones por día
- Necesitas **alta disponibilidad** (el servicio no puede caerse)
- Tienes **múltiples servicios** que necesitan coordinarse
- Equipo de infraestructura que lo mantenga

## ¿Cuándo NO lo necesitas?

- Proyecto personal o pequeña empresa
- Pocas peticiones (un solo contenedor es suficiente)
- No tienes experiencia en infraestructura
- Puedes usar servicios administrados (Cloud Run, App Service, etc.)

## Alternativas más simples para escalar

| Solución | Complejidad | Cuándo usarla |
|----------|-------------|---------------|
| Docker solo | Baja | Desarrollo, pocos usuarios |
| Docker Compose | Baja-Media | Múltiples servicios locales |
| Cloud Run (Google) | Baja | Escalar sin gestionar K8s |
| AWS ECS/Fargate | Media | Escalar contenedores en AWS |
| Kubernetes | Alta | Enterprise, mucho tráfico |

## Conclusión

Para el 90% de proyectos de ML en empresas medianas, **Docker + un servicio cloud administrado** es suficiente. Kubernetes es poderoso pero complejo. Aprenderlo es valioso si te interesa la infraestructura, pero no es requisito para desplegar modelos de ML.

---

**Volver al módulo**: [README](README.md)
