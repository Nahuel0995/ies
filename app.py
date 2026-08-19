import streamlit as st

from preguntas import (
    obtener_preguntas_mezcladas
)

from evaluacion import (
    obtener_resultado,
    ORIENTACIONES
)

from base_datos import (
    guardar_resultado
)


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(

    page_title=
        "Test Vocacional IES N.º 11",

    page_icon="🎓",

    layout="centered"
)


# ==========================================================
# ESTILOS
# ==========================================================

# ==========================================================
# ESTILOS
# ==========================================================

st.markdown(
"""
<style>

/* Ocultar elementos predeterminados de Streamlit para aspecto de App */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Fondo general de la aplicación en blanco/gris muy claro */
.stApp {
    background-color: #F4F6F9;
}

/* Contenedor principal estilo tarjeta flotante */
.block-container {
    max-width: 750px;
    padding: 2.5rem;
    background-color: #FFFFFF; /* Fondo blanco para el contenido */
    border-radius: 15px;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.08); /* Sombra suave */
    border-top: 8px solid #0033A0; /* Línea azul superior institucional */
    margin-top: 3rem;
    margin-bottom: 3rem;
}

/* Botones principales: Azul Institucional */
/* Botones principales: Azul Institucional */
.stButton > button {
    width: 100%;
    min-height: 60px;
    border-radius: 10px;
    font-size: 20px !important;
    font-weight: 900 !important; /* <--- LETRA MUY FUERTE/NEGRITA */
    background-color: #0033A0 !important; 
    color: #FFFFFF !important; 
    border: none;
    transition: all 0.3s ease;
    box-shadow: 0px 4px 6px rgba(0, 51, 160, 0.2);
}

/* Efecto hover en botones (Azul más claro) */
.stButton > button:hover {
    background-color: #0055FF !important;
    transform: translateY(-2px);
    box-shadow: 0px 6px 12px rgba(0, 85, 255, 0.3);
}

/* Tarjetas de resultados */
.resultado {
    padding: 20px;
    background: #FFFFFF;
    border-left: 6px solid #0033A0; /* Borde izquierdo azul */
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

/* Títulos y subtítulos en azul oscuro */
h1, h2, h3 {
    color: #002266 !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Texto general */
p, span, label {
    color: #333333 !important;
}

/* Color de las barras de progreso */
.stProgress > div > div > div > div {
    background-color: #0055FF;
}

</style>
""",
unsafe_allow_html=True
)

# ==========================================================
# INICIALIZAR
# ==========================================================

if "pagina" not in st.session_state:

    st.session_state.pagina = "inicio"


if "preguntas" not in st.session_state:

    st.session_state.preguntas = (
        obtener_preguntas_mezcladas()
    )


if "pregunta_actual" not in st.session_state:

    st.session_state.pregunta_actual = 0


if "respuestas" not in st.session_state:

    st.session_state.respuestas = {}


if "resultado_guardado" not in st.session_state:

    st.session_state.resultado_guardado = False


# ==========================================================
# REINICIAR
# ==========================================================

def reiniciar():

    for key in list(
        st.session_state.keys()
    ):

        del st.session_state[key]


    st.session_state.pagina = "inicio"

    st.session_state.preguntas = (
        obtener_preguntas_mezcladas()
    )

    st.rerun()


# ==========================================================
# INICIO
# ==========================================================

if st.session_state.pagina == "inicio":
    try:
        st.image("logo ies.jpg", width=200) 
    except FileNotFoundError:
        st.warning("No se encontró la imagen del logo (logo_ies11.png).")
    st.title("🎓 IES N.º 11")

    st.header(
        "Test Vocacional"
    )


    st.write(
        "Descubrí qué áreas y "
        "tecnicaturas podrían ser "
        "afines a tus intereses."
    )


    st.info(
        "📱 Diseñado para realizarse "
        "desde el celular.\n\n"
        "⏱️ Tiempo estimado: 3 a 5 minutos."
    )


    st.warning(
        "El resultado es orientativo y "
        "no determina qué carrera debés estudiar."
    )


    if st.button(
        "🚀 COMENZAR TEST"
    ):

        st.session_state.pagina = "datos"

        st.rerun()


# ==========================================================
# DATOS
# ==========================================================

elif st.session_state.pagina == "datos":

    st.title(
        "👤 Datos del participante"
    )


    nombre = st.text_input(
        "Nombre"
    )


    apellido = st.text_input(
        "Apellido"
    )


    edad = st.number_input(

        "Edad",

        min_value=13,

        max_value=100,

        value=18,

        step=1
    )
    email = st.text_input("Correo Electrónico")

    sexo = st.selectbox(

        "Sexo",

        [
            "Femenino",
            "Masculino",
            "Prefiero no responder"
        ]
    )


    if st.button(
        "CONTINUAR ➡️"
    ):

        if (
            not nombre.strip()
            or
            not apellido.strip()
        ):

            st.error(
                "Completá nombre y apellido."
            )

        else:

            st.session_state.nombre = (
                nombre.strip()
            )

            st.session_state.apellido = (
                apellido.strip()
            )
            st.session_state.email = email.strip()

            st.session_state.edad = int(
                edad
            )

            st.session_state.sexo = sexo

            st.session_state.pagina = "test"

            st.rerun()


# ==========================================================
# TEST
# ==========================================================

elif st.session_state.pagina == "test":

    total = len(st.session_state.preguntas)
    actual = st.session_state.pregunta_actual
    pregunta = st.session_state.preguntas[actual]

    # Cálculo del progreso y porcentaje
    avance = (actual + 1) / total
    porcentaje = int(avance * 100)

    st.progress(avance)
    
    # Mostrar texto con porcentaje en negrita
    st.markdown(f"**Pregunta {actual + 1} de {total} — {porcentaje}% completado**")

    st.subheader(pregunta["pregunta"])
    st.write("¿Cuánto te interesa?")

    # Recuperar respuesta previa si el usuario vuelve atrás
    valor_previo = st.session_state.respuestas.get(pregunta["id"], 3)
    indice_previo = [1, 2, 3, 4, 5].index(valor_previo)

    respuesta = st.radio(
        "Seleccioná una opción:",
        [1, 2, 3, 4, 5],
        index=indice_previo, # Mantiene marcada la respuesta anterior
        format_func=lambda x: {
            1: "1 — No me interesa",
            2: "2 — Me interesa poco",
            3: "3 — Me interesa moderadamente",
            4: "4 — Me interesa bastante",
            5: "5 — Me interesa mucho"
        }[x],
        key=f"respuesta_{pregunta['id']}"
    )

    st.write("") # Espacio en blanco

    # Crear dos columnas para los botones "Anterior" y "Siguiente"
    col1, col2 = st.columns(2)

    with col1:
        # Solo mostrar "Anterior" si NO estamos en la primera pregunta
        if actual > 0:
            if st.button("⬅️ ANTERIOR"):
                st.session_state.pregunta_actual -= 1
                st.rerun()

    with col2:
        if actual < total - 1:
            if st.button("SIGUIENTE ➡️"):
                st.session_state.respuestas[pregunta["id"]] = respuesta
                st.session_state.pregunta_actual += 1
                st.rerun()
        else:
            if st.button("🎯 VER MI RESULTADO"):
                st.session_state.respuestas[pregunta["id"]] = respuesta
                st.session_state.pagina = "resultado"
                st.rerun()


# ==========================================================
# RESULTADO
# ==========================================================

elif st.session_state.pagina == "resultado":

    resultado = obtener_resultado(

        st.session_state.respuestas,

        st.session_state.preguntas
    )


    # ----------------------------------
    # GUARDAR
    # ----------------------------------

    if not st.session_state.resultado_guardado:

        numero = guardar_resultado(

            st.session_state.nombre,

            st.session_state.apellido,
            st.session_state.email,

            st.session_state.edad,

            st.session_state.sexo,

            st.session_state.respuestas,

            resultado
        )


        st.session_state.numero_registro = (
            numero
        )


        st.session_state.resultado_guardado = True


    # ----------------------------------
    # RESULTADO
    # ----------------------------------

    st.title(
        "🎯 Tu resultado"
    )


    st.write(
        f"¡Gracias, **{st.session_state.nombre}**!"
    )


    tipo = resultado[
        "tipo_perfil"
    ]


    principal = resultado[
        "perfil_principal"
    ]


    secundario = resultado[
        "perfil_secundario"
    ]


    # ----------------------------------
    # PERFIL DEFINIDO
    # ----------------------------------

    if tipo == "definido":

        nombre_perfil = (
            ORIENTACIONES[
                principal[0]
            ]["nombre"]
        )


        st.success(
            f"### {nombre_perfil}"
        )


        st.write(
            ORIENTACIONES[
                principal[0]
            ]["descripcion"]
        )


    # ----------------------------------
    # PERFIL COMBINADO
    # ----------------------------------

    elif tipo == "combinado":

        p1 = ORIENTACIONES[
            principal[0]
        ]["nombre"]


        p2 = ORIENTACIONES[
            secundario[0]
        ]["nombre"]


        st.success(
            "### 🔀 Perfil combinado"
        )


        st.subheader(
            f"{p1} + {p2}"
        )


        st.write(
            "Tus respuestas muestran "
            "intereses importantes en "
            "dos áreas diferentes."
        )


    # ----------------------------------
    # PERFIL EXPLORADOR
    # ----------------------------------

    else:

        st.success(
            "### 🌈 Perfil explorador"
        )


        st.write(
            "Tus intereses aparecen "
            "bastante distribuidos entre "
            "las distintas áreas."
        )


    # ----------------------------------
    # ORIENTACIONES
    # ----------------------------------

    st.divider()


    st.subheader(
        "📊 Tus áreas de afinidad"
    )


    for (
        orientacion,
        porcentaje
    ) in resultado[
        "ranking_orientaciones"
    ]:

        st.write(
            ORIENTACIONES[
                orientacion
            ]["nombre"]
        )


        st.progress(
            int(porcentaje)
        )


        st.caption(
            f"{porcentaje:.0f}%"
        )


    # ----------------------------------
    # CARRERAS
    # ----------------------------------

    st.divider()


    st.header(
        "🎓 Tecnicaturas que podrías explorar"
    )


    st.write(
        "Estas carreras presentan "
        "mayor afinidad con tus respuestas:"
    )


    for (
        posicion,
        carrera
    ) in enumerate(

        resultado["top4"],

        start=1
    ):

        st.markdown(

            f"""
            <div class="resultado">

            <h3>
            {posicion}️⃣
            {carrera["carrera"]}
            </h3>

            <strong>
            Afinidad:
            {carrera["afinidad"]:.0f}%
            </strong>

            <p>
            {carrera["descripcion"]}
            </p>

            </div>
            """,

            unsafe_allow_html=True
        )


    st.divider()


    st.success(

        f"Registro: "
        f"IES11-"
        f"{st.session_state.numero_registro:04d}"
    )


    st.caption(
        "Este resultado es orientativo. "
        "Su objetivo es ayudarte a explorar "
        "posibles áreas de estudio."
    )


    if st.button(
        "🔄 REALIZAR OTRO TEST"
    ):

        reiniciar()
