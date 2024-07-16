import streamlit as st
import pandas as pd

# Configura el título de la aplicación
st.title("Formulario de Seguimiento de Lección de Piano")

# Cargar datos existentes del CSV, si existen
try:
    df_evaluaciones = pd.read_csv("evaluaciones_lecciones.csv")
except FileNotFoundError:
    df_evaluaciones = pd.DataFrame(
        columns=[
            "Nombre del Estudiante",
            "Edad",
            "Nivel",
            "Dificultad de la Tarea",
            "Empeño del Estudiante",
            "Empeño del Profesor",
            "Aprendizaje del Estudiante",
            "Aprendizaje del Profesor",
            "Aspectos Técnicos",
            "Fecha de la Lección",
            "Teoría Deseada",
            "Piano Deseado",
        ]
    )

# Crea un formulario con Streamlit
with st.form("lesson_form"):
    st.write("**Información del Estudiante**")
    nombre_estudiante = st.text_input("Nombre del Estudiante:")
    edad_estudiante = st.number_input("Edad:", min_value=0, step=1)
    nivel_estudiante = st.selectbox(
        "Nivel:", ["Principiante", "Intermedio", "Avanzado"]
    )

    st.write("**Evaluación de la Lección**")
    dificultad_tarea = st.slider(
        "Dificultad de la tarea (1-7):", min_value=1, max_value=7, value=4
    )
    empeno_estudiante = st.slider(
        "Empeño del estudiante (1-7):", min_value=1, max_value=7, value=4
    )
    empeno_profesor = st.slider(
        "Empeño del profesor (1-7):", min_value=1, max_value=7, value=4
    )

    aprendido_estudiante = st.text_area("¿Qué aprendiste hoy? (Estudiante):")
    aprendido_profesor = st.text_area("¿Qué se trabajó hoy? (Profesor):")
    sesion_tecnica = st.text_input(
        "¿Cómo estuvo la sesión técnicamente? (Internet, fluidez, etc.):"
    )
    fecha_leccion = st.date_input("Fecha de la Lección:")
    teoria_deseada = st.text_input(
        "¿Qué te gustaría ver en teoría? (Estudiante):"
    )
    piano_deseado = st.text_input(
        "¿Qué te gustaría ver en piano? (Estudiante):"
    )

    # Botón de envío
    submitted = st.form_submit_button("Guardar Evaluación")

# Maneja el envío del formulario
if submitted:
    # Crea un diccionario con los datos del formulario
    data = {
        "Nombre del Estudiante": nombre_estudiante,
        "Edad": edad_estudiante,
        "Nivel": nivel_estudiante,
        "Dificultad de la Tarea": dificultad_tarea,
        "Empeño del Estudiante": empeno_estudiante,
        "Empeño del Profesor": empeno_profesor,
        "Aprendizaje del Estudiante": aprendido_estudiante,
        "Aprendizaje del Profesor": aprendido_profesor,
        "Aspectos Técnicos": sesion_tecnica,
        "Fecha de la Lección": fecha_leccion,
        "Teoría Deseada": teoria_deseada,
        "Piano Deseado": piano_deseado,
    }

    # Agrega la nueva evaluación al DataFrame
    df_evaluaciones = df_evaluaciones.append(data, ignore_index=True)

    # Guarda el DataFrame actualizado en el archivo CSV
    df_evaluaciones.to_csv("evaluaciones_lecciones.csv", index=False)

    # Muestra un mensaje de éxito
    st.success("¡Evaluación guardada con éxito!")

# Muestra la tabla con las evaluaciones (solo fecha y estudiante)
st.write("## Evaluaciones Guardadas")
st.dataframe(df_evaluaciones[["Fecha de la Lección", "Nombre del Estudiante"]])

# Crea un botón para descargar el DataFrame como CSV
st.download_button(
    label="Descargar Evaluaciones (CSV)",
    data=df_evaluaciones.to_csv(index=False),
    file_name="evaluaciones_lecciones.csv",
    mime="text/csv",
)