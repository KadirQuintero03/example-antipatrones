# Ejemplo de Antipatrón Golden Hammer y Solución con Clean Architecture

## Contexto del Problema

El desarrollador "Juanito" recibió la asignación en su empresa de crear un microservicio para procesar archivos CSV con datos de temperatura de diferentes ciudades. Sin ganas de implementar algo que pudiera tomarle más tiempo y sin intención de aprender nuevas herramientas, Juanito implementó este microservicio usando únicamente JavaScript (porque es el único lenguaje que conoce), una arquitectura de carpetas MVC (porque le pareció perfecta, siendo la única que ha utilizado) y basándose en programación procedural.

### Requerimientos del microservicio
- Recibir archivos CSV con datos meteorológicos
- Convertir los datos a formato JSON
- Almacenar la información en archivos JSON
- Proporcionar endpoints para consultar datos históricos

## Antipatrón: Golden Hammer

El Golden Hammer ocurre cuando un desarrollador usa siempre la misma tecnología o patrón, sin considerar si es la mejor opción para el problema. En este caso, Juanito usó JavaScript y MVC para todo, aunque no es óptimo para procesamiento de datos científicos.

### Ejemplo de mala implementación (JS + MVC + procedural)
- Todo el procesamiento de datos se hace con JS y Express.
- No hay separación clara de responsabilidades ni uso de herramientas científicas.
- El código es difícil de escalar y mantener para análisis avanzados.

## Solución: Clean Architecture + SOLID en Python

Se reimplementó el microservicio usando Python, aplicando Clean Architecture y principios SOLID:
- **Separación de responsabilidades:** Repositorios para acceso a datos, casos de uso para lógica de negocio, rutas para interacción con el usuario.
- **Inyección de dependencias:** Permite cambiar fácilmente la fuente de datos o la lógica sin modificar el resto del sistema.
- **Uso de librerías científicas:** Se utiliza pandas para procesar los CSV de forma eficiente.
- **Escalabilidad y mantenibilidad:** El sistema es fácil de extender y probar.

## Estructura de Carpetas

```
js-mvc/
  app.js
  controllers/
    dataController.js
  models/
    dataModel.js
  views/
    routes.js
python-clean/
  app/
    main.py
    repositories/
      csv_repository.py
      json_repository.py
    usecases/
      process_csv_usecase.py
      get_historical_usecase.py
```

## ¿Por qué es mejor la solución en Python?
- Permite procesamiento avanzado de datos.
- Facilita la escalabilidad y el mantenimiento.
- Aplica buenas prácticas de arquitectura y diseño.

---

**Conclusión:**

Evita el Golden Hammer: elige la tecnología y el patrón adecuados para cada problema. La solución en Python con Clean Architecture es más robusta, flexible y profesional para procesamiento de datos científicos.
