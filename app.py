"""Prototipo académico de clasificación de estrategias pedagógicas.
Los datos sintéticos no validan pertinencia pedagógica real.
"""
from pathlib import Path
import json
import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="Asistente IA | Planificación Docente", page_icon="🎓", layout="wide")
st.title("🎓 Asistente de Inteligencia Artificial para la Planificación Docente")
st.caption("Proyecto final de Machine Learning · UFHEC · Prototipo educativo experimental")
st.warning("Demostración experimental: el modelo fue entrenado con 480 escenarios **sintéticos** etiquetados mediante reglas. No está validado por docentes ni debe emplearse como decisión pedagógica automática.")

@st.cache_resource
def load_model():
    return joblib.load(ROOT / "modelos" / "clasificador_estrategias.joblib")

@st.cache_data
def load_data():
    data = pd.read_csv(ROOT / "data" / "escenarios_sinteticos.csv")
    results = json.loads((ROOT / "data" / "metricas.json").read_text(encoding="utf-8"))
    return data, results

model = load_model()
df, metrics = load_data()
landing, analysis, models, demo, docs = st.tabs([
    "🏠 Proyecto", "📊 Datos y análisis", "🧠 Modelo y métricas", "📝 Probar asistente", "📚 Documentación"
])

with landing:
    st.header("¿Qué problema queremos resolver?")
    st.write("La planificación de una clase requiere articular competencias, contenidos, estrategias, recursos y evaluación. Este ejercicio explora cómo una clasificación supervisada puede ayudar a **sugerir una estrategia** y crear un **borrador editable** sujeto a revisión del docente.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Escenarios sintéticos", len(df))
    col2.metric("Estrategias posibles", df['estrategia'].nunique())
    col3.metric("Modelos comparados", len(metrics['modelos']))
    st.subheader("Flujo del sistema")
    st.info("Formulario docente → codificación de variables → modelo supervisado → recomendación → plantilla de planificación → revisión humana")
    st.write("**Pregunta de investigación:** ¿Cómo puede un clasificador supervisado de estrategias pedagógicas apoyar la elaboración de borradores de planificación docente?")
    st.write("**Alcance:** prueba de viabilidad técnica con datos simulados. La aplicación no integra un modelo de lenguaje generativo.")

with analysis:
    st.header("Análisis exploratorio de los datos")
    st.write("Dataset generado para el ejercicio. Ningún registro describe a estudiantes o docentes reales.")
    st.dataframe(df.head(12), use_container_width=True)
    st.subheader("Frecuencia de estrategias")
    st.bar_chart(df['estrategia'].value_counts().rename_axis('Estrategia').to_frame('Casos'))
    st.subheader("Distribución por nivel educativo")
    st.bar_chart(df['nivel'].value_counts().rename_axis('Nivel').to_frame('Casos'))
    st.write(f"**Valores faltantes:** {int(df.isna().sum().sum())} · **Registros duplicados:** {int(df.duplicated().sum())}")
    st.caption("Los gráficos describen ejemplos generados, no estadísticas de centros educativos de República Dominicana.")

with models:
    st.header("Entrenamiento y resultados")
    st.write("Se compararon Regresión Logística y Random Forest, con separación estratificada 75 % entrenamiento / 25 % prueba y validación cruzada sobre entrenamiento.")
    table = pd.DataFrame(metrics['modelos']).rename(columns={
        'modelo':'Modelo', 'cv_f1_macro_mean':'F1 macro (CV)',
        'test_accuracy':'Accuracy (prueba)', 'test_precision_macro':'Precisión macro',
        'test_recall_macro':'Recall macro', 'test_f1_macro':'F1 macro (prueba)'
    })
    st.dataframe(table, use_container_width=True, hide_index=True)
    st.write("**Modelo almacenado:** Random Forest")
    st.subheader("Matriz de confusión — conjunto de prueba")
    confusion = pd.DataFrame(metrics['matriz_confusion'], index=metrics['clases'], columns=metrics['clases'])
    st.dataframe(confusion, use_container_width=True)
    st.error("**Interpretación crítica:** F1 = 1.00 no significa que el sistema acierte al recomendar estrategias en aulas reales. Las etiquetas del dataset proceden de reglas deterministas, por lo que el experimento solo comprueba la capacidad de reproducir esas reglas.")
    st.write("Para una validación educativa se requieren casos autorizados, etiquetas consensuadas por especialistas y una prueba independiente con docentes.")

with demo:
    st.header("Probar el prototipo")
    with st.form("plan_docente"):
        a, b = st.columns(2)
        with a:
            nivel = st.selectbox("Nivel educativo", ["Primaria", "Secundaria", "Superior"])
            asignatura = st.selectbox("Asignatura", ["Matemáticas", "Lengua Española", "Ciencias Naturales", "Ciencias Sociales"])
            tema = st.text_input("Tema", "Las fracciones")
            objetivo = st.text_input("Objetivo de aprendizaje", "Identificar fracciones sencillas")
        with b:
            necesidad = st.selectbox("Necesidad del grupo", ["Refuerzo", "Colaboración", "Aplicación", "Profundización"])
            contenido = st.selectbox("Tipo de contenido", ["Conceptual", "Procedimental", "Contextual"])
            recursos = st.selectbox("Recursos", ["Manipulativos", "Básicos", "Digitales"])
            duracion = st.selectbox("Duración", [45, 60, 90])
        submit = st.form_submit_button("Generar recomendación", type="primary")
    if submit:
        inputs = pd.DataFrame([{'nivel':nivel, 'asignatura':asignatura,
            'necesidad':necesidad, 'tipo_contenido':contenido,
            'recursos':recursos, 'duracion_min':duracion}])
        strategy = str(model.predict(inputs)[0])
        st.success(f"Estrategia recomendada por el modelo: **{strategy}**")
        start = max(5, round(duracion * .2))
        middle = round(duracion * .6)
        end = duracion - start - middle
        plan = (f"PLANIFICACIÓN DOCENTE (BORRADOR EXPERIMENTAL)\n"
                f"Nivel: {nivel}\nAsignatura: {asignatura}\nTema: {tema}\n"
                f"Objetivo: {objetivo}\nEstrategia: {strategy}\nRecursos: {recursos}\n"
                f"INICIO ({start} min): recuperar conocimientos previos mediante preguntas sobre {tema}.\n"
                f"DESARROLLO ({middle} min): presentar ejemplos y practicar con la estrategia {strategy.lower()}; dar apoyo y retroalimentación.\n"
                f"CIERRE ({end} min): síntesis de aprendizajes y preguntas de salida.\n"
                f"EVALUACIÓN: lista de cotejo sobre comprensión, participación y actividad práctica.\n"
                f"NOTA: revisar y adaptar todo el contenido antes de aplicarlo en clase.\n")
        st.text_area("Borrador editable para copiar o revisar", value=plan, height=310)
        st.download_button("Descargar borrador TXT", plan, file_name="planificacion_docente.txt", mime="text/plain")
        st.caption("La estrategia proviene del clasificador entrenado; el texto del plan se produce mediante una plantilla programada, no IA generativa.")

with docs:
    st.header("Documentación y reproducibilidad")
    st.markdown("**Notebook:** `notebooks/Proyecto_ML_Planificacion_Docente.ipynb`  \n**Informe PDF:** `documentos/Informe_Tecnico_Final.pdf`  \n**CSV:** `data/escenarios_sinteticos.csv`  \n**Código:** `app.py`  \n**Métricas:** `data/metricas.json`")
    st.write("El repositorio contiene las instrucciones de instalación, la procedencia de los datos y las limitaciones del ejercicio.")
    st.write("**Privacidad y ética:** no ingresar datos identificables de estudiantes, no interpretar la recomendación como una validación pedagógica y exigir revisión profesional.")
