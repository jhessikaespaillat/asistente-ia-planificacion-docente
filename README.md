# Datos sintéticos de práctica

`escenarios_sinteticos.csv`: 480 registros artificiales generados programáticamente, sin participación de docentes ni información de estudiantes. Las etiquetas **no** representan consenso pedagógico. Cada etiqueta se deriva directamente de `necesidad`: Refuerzo → Práctica guiada; Colaboración → Aprendizaje cooperativo; Aplicación → Aprendizaje basado en problemas; Profundización → Proyecto de profundización. Esto crea una tarea trivial de clasificación; F1=1 no indica utilidad real. Para investigación futura se requieren datos autorizados, acuerdos de etiquetado y validación independiente.

## Aplicación web publicada

El Asistente de Inteligencia Artificial para la Planificación Docente se encuentra disponible en Streamlit Community Cloud.

[Abrir aplicación en Streamlit](https://asistente-ia-planificacion-docente-exzs7ckpwvpogrmyshh82v.streamlit.app/)

La aplicación permite explorar los datos, consultar los resultados de los modelos y generar un borrador experimental de planificación docente.
## Cuaderno Jupyter

El cuaderno contiene el análisis de 480 escenarios sintéticos, el entrenamiento de Regresión Logística y Random Forest y la evaluación del modelo seleccionado.

[Ver cuaderno Jupyter](https://github.com/jhessikaespaillat/asistente-ia-planificacion-docente/blob/main/Proyecto_ML_Planificacion_Docente.ipynb)
