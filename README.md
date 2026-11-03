# Asistente de Inteligencia Artificial para la Planificación Docente

**Proyecto académico – UFHEC | Área: Tecnología e Innovación Educativa**

## Problema
La planificación de clases puede consumir mucho tiempo y dificultar la selección de estrategias diferenciadas según las necesidades del grupo.

## Objetivo
Diseñar una solución que sugiera estrategias pedagógicas a partir de características de una clase y facilite la elaboración de borradores de planificación que deberán ser revisados por el docente.

## Alcance de esta versión
Este repositorio incluye el documento de diseño y un **prototipo demostrativo basado en reglas**. **No hay un modelo de Machine Learning entrenado ni un servicio de IA generativa conectado**. El módulo de ML supervisado se propone como fase futura, sujeto a disponibilidad de datos etiquetados y validación pedagógica.

## Cómo ejecutar la demostración
1. Instala Python 3.10 o posterior.
2. Abre una terminal en esta carpeta.
3. Ejecuta `pip install -r requirements.txt`.
4. Ejecuta `streamlit run app.py`.

## Estructura
- `app.py`: demostración interactiva de recomendaciones y borrador de planificación.
- `requirements.txt`: dependencias.
- `documentos/`: entrega académica en Word.

## Propuesta de Machine Learning
- **Variable objetivo**: estrategia pedagógica recomendada.
- **Variables de entrada**: nivel educativo, competencia, tipo de contenido y necesidad educativa identificada.
- **Modelo candidato**: clasificación supervisada (árbol de decisión o Random Forest), sujeto a comparación y evaluación con datos reales y etiquetas validadas por docentes.
- **Evaluación futura**: precisión, recall, F1, matriz de confusión y validación por especialistas.

## Consideraciones éticas
No ingresar nombres ni datos identificables de estudiantes. Las sugerencias requieren revisión profesional y no sustituyen las decisiones del docente.

## Estado
Versión inicial para documentación y demostración; no corresponde a una herramienta validada para uso institucional.
