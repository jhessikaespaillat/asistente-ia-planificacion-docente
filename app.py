"""Prototipo académico: reglas explícitas, NO modelo ML entrenado."""
import streamlit as st

st.set_page_config(page_title="Asistente IA | Planificación docente", page_icon="📚")
st.title("📚 Asistente para la Planificación Docente")
st.caption("Prototipo educativo basado en reglas. No utiliza aún un modelo entrenado ni IA generativa.")
st.info("Usa información general del grupo. No incluyas datos personales de estudiantes.")

with st.form("plan"):
    asignatura = st.text_input("Asignatura", "Ciencias Naturales")
    nivel = st.selectbox("Nivel educativo", ["Primaria", "Secundaria", "Superior"])
    tema = st.text_input("Tema de la clase", "El ciclo del agua")
    competencia = st.selectbox("Competencia principal", ["Comprensión", "Resolución de problemas", "Colaboración", "Pensamiento crítico"])
    necesidad = st.selectbox("Necesidad del grupo", ["Refuerzo", "Nivel heterogéneo", "Profundización", "Sin necesidad específica"])
    duracion = st.number_input("Duración (minutos)", min_value=20, max_value=240, value=50, step=5)
    enviado = st.form_submit_button("Generar propuesta")

if enviado:
    if necesidad == "Refuerzo":
        estrategia, actividad = "Enseñanza guiada y práctica gradual", "Explicación breve, ejemplo resuelto y ejercicios con apoyo progresivo."
    elif necesidad == "Profundización":
        estrategia, actividad = "Aprendizaje basado en proyectos", "Planteamiento de un reto de ampliación con producto y justificación."
    elif competencia == "Colaboración":
        estrategia, actividad = "Aprendizaje cooperativo", "Equipos pequeños con roles definidos y producto colectivo."
    elif competencia == "Resolución de problemas":
        estrategia, actividad = "Aprendizaje basado en problemas", "Análisis de una situación y comparación de soluciones."
    elif competencia == "Pensamiento crítico":
        estrategia, actividad = "Estudio de caso", "Discusión de evidencias y argumentación de conclusiones."
    else:
        estrategia, actividad = "Aprendizaje activo con evaluación formativa", "Activación de conocimientos previos, trabajo aplicado y reflexión final."
    inicio = round(duracion * 0.2)
    cierre = round(duracion * 0.2)
    desarrollo = duracion - inicio - cierre
    st.subheader("Propuesta de planificación para revisión")
    st.write(f"**Asignatura:** {asignatura} | **Nivel:** {nivel} | **Tema:** {tema}")
    st.write(f"**Competencia:** {competencia} | **Estrategia sugerida:** {estrategia}")
    st.write(f"**Inicio ({inicio} min):** preguntas diagnósticas y presentación del propósito de la clase.")
    st.write(f"**Desarrollo ({desarrollo} min):** {actividad}")
    st.write(f"**Cierre ({cierre} min):** síntesis, preguntas de salida y autoevaluación.")
    st.write("**Evaluación sugerida:** lista de cotejo o rúbrica sencilla alineada con la competencia.")
    st.warning("Esta salida es una plantilla orientativa basada en reglas. El docente debe ajustarla al currículo y a la realidad de su grupo.")
