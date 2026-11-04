# Asistente de Inteligencia Artificial para la Planificación Docente

**Proyecto final de Machine Learning | UFHEC | Aprendizaje Automático (IAE-2501)**  
**Autora:** Jhessika Lidabed Espaillat Espaillat  
**Estado:** Prototipo experimental académico. **No validado para uso en aulas.**

## Resumen
Esta solución experimental clasifica estrategias pedagógicas a partir de los atributos de una solicitud docente y produce un borrador de planificación mediante plantillas. Atiende a la necesidad de agilizar la preparación de clases, **sin reemplazar el juicio profesional docente**.

## Problema y objetivo
La planificación exige seleccionar objetivos, actividades, estrategias y evaluaciones adaptadas al grupo. **Objetivo:** explorar la viabilidad técnica de un clasificador supervisado de estrategias y mostrar su integración en una interfaz sencilla.

## Pregunta de investigación
¿Cómo puede un clasificador supervisado de estrategias pedagógicas apoyar la elaboración de borradores de planificación docente sujetos a revisión humana?

## Datos y metodología
- **Archivo:** `data/escenarios_sinteticos.csv`, 480 registros sintéticos creados para el ejercicio, sin datos de alumnos reales.
- **Entradas:** nivel, asignatura, necesidad, tipo de contenido, recursos y duración.
- **Objetivo:** estrategia (práctica guiada, aprendizaje cooperativo, aprendizaje basado en problemas, proyecto de profundización).
- **Proceso:** limpieza/inspección EDA → OneHotEncoder → separación 75/25 estratificada → validación cruzada 5-fold sobre entrenamiento → comparación de regresión logística y Random Forest → prueba final.
- **Modelo:** `modelos/clasificador_estrategias.joblib` (archivo generado localmente, no descargar modelos de fuentes no confiables).
- **Notebook reproducible:** `notebooks/Proyecto_ML_Planificacion_Docente.ipynb`.

## Resultados obtenidos y limitación crítica
Ambos clasificadores obtuvieron **F1-macro = 1.00** en el conjunto sintético de prueba y en validación cruzada. **Esto es esperable y no acredita precisión real**: las etiquetas se derivan de una relación determinista simple con la variable `necesidad`. El modelo reproduce la regla creada para el ejercicio, no ha aprendido preferencias de especialistas ni ha sido probado en entornos educativos. Se necesita recolectar escenarios autorizados, etiquetar por expertos y evaluar utilidad y sesgos.

## Secciones de la aplicación
La landing page incluye presentación del problema, vista exploratoria con gráficos, comparación de modelos y métricas, formulario de predicción y acceso a la documentación.

## Arquitectura
`Formulario Streamlit → codificación de variables → clasificador entrenado → estrategia recomendada → plantilla de borrador → revisión del docente`.

## Ejecutar en computadora
```bash
pip install -r requirements.txt
streamlit run app.py
```
El notebook se puede abrir en Google Colab. Si no se ejecuta desde la raíz del repositorio, cargar manualmente el archivo CSV indicado en el notebook.

## Publicar en Streamlit Community Cloud
Crear una aplicación desde el repositorio GitHub con rama `main` y archivo principal `app.py`. Luego copiar el enlace público y agregarlo a esta sección.

**Enlace a aplicación:** PENDIENTE DE PUBLICACIÓN POR LA ESTUDIANTE (actualizar después de Deploy).  
**Enlace a video:** PENDIENTE DE GRABACIÓN Y PUBLICACIÓN POR LA ESTUDIANTE.

## Documentación
- `documentos/Informe_Tecnico_Final.pdf` — problema, metodología, métricas, ética y referencias.
- `documentos/Informe_Tecnico_Final.docx` — edición de informe.
- `video/Guion_y_Pasos_Video.md` — guion y guía de elaboración del video automatizado.

## Consideraciones éticas
No introducir datos personales identificables de estudiantes. Las etiquetas sintéticas y el alcance experimental se anuncian de manera explícita. Toda planificación debe ser revisada por un profesional; se requieren pruebas externas para concluir utilidad pedagógica.

## Referencias básicas
- Documentación scikit-learn: https://scikit-learn.org/stable/
- Streamlit: https://docs.streamlit.io/
- GitHub: https://docs.github.com/
- Materiales y plantilla entregados en clase por el docente.
