import streamlit as st
from pathlib import Path  # <--- ¡AGREGA ESTA LÍNEA!


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
# RUTAS
# ==========================================================

RUTA_BASE = Path(__file__).parent

RUTA_LOGO = (
    RUTA_BASE
    / "imagenes"
    / "logo ies.jpg"
)

RUTA_FOTO = (
    RUTA_BASE
    / "imagenes"
    / "ies-n-11.webp"
)


# ==========================================================
# ESTILOS
# ==========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       CONTENEDOR GENERAL
    ===================================================== */

    .block-container {

        max-width: 760px;

        margin-left: auto;
        margin-right: auto;

        padding-left: 1rem;
        padding-right: 1rem;

        padding-bottom: 2rem;
    }


    /* =====================================================
       BOTONES GENERALES
    ===================================================== */

    .stButton > button {

        width: 100%;

        min-height: 54px;

        border-radius: 14px;

        font-size: 1.05rem;

        font-weight: 700;

        border: none;

        transition:
            transform 0.15s ease,
            box-shadow 0.15s ease;
    }


    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 8px 20px
            rgba(
                0,
                0,
                0,
                0.20
            );
    }


    /* =====================================================
       BOTÓN CONTINUAR DEL FORMULARIO
    ===================================================== */

    div[data-testid="stFormSubmitButton"] > button {

        width: 100% !important;

        min-height: 56px !important;

        background:
            linear-gradient(
                135deg,
                #2563EB,
                #1D4ED8
            ) !important;

        color: #FFFFFF !important;

        border:
            1px solid
            #60A5FA !important;

        border-radius: 14px !important;

        font-size: 1.05rem !important;

        font-weight: 800 !important;

        box-shadow:
            0 8px 22px
            rgba(
                37,
                99,
                235,
                0.28
            ) !important;

        transition:
            transform 0.15s ease,
            box-shadow 0.15s ease,
            background 0.15s ease !important;
    }


    /* TEXTO E ICONO DEL BOTÓN */

    div[data-testid="stFormSubmitButton"] > button p {

        color: #FFFFFF !important;

        font-size: 1.05rem !important;

        font-weight: 800 !important;

        margin: 0 !important;
    }


    /* HOVER DEL BOTÓN CONTINUAR */

    div[data-testid="stFormSubmitButton"] > button:hover {

        background:
            linear-gradient(
                135deg,
                #1D4ED8,
                #1E40AF
            ) !important;

        color: #FFFFFF !important;

        border-color:
            #93C5FD !important;

        transform:
            translateY(-2px);

        box-shadow:
            0 10px 25px
            rgba(
                29,
                78,
                216,
                0.35
            ) !important;
    }


    div[data-testid="stFormSubmitButton"] > button:hover p {

        color: #FFFFFF !important;
    }


    /* FOCUS */

    div[data-testid="stFormSubmitButton"] > button:focus {

        color: #FFFFFF !important;

        border-color:
            #93C5FD !important;

        box-shadow:
            0 0 0 3px
            rgba(
                147,
                197,
                253,
                0.40
            ) !important;
    }


    div[data-testid="stFormSubmitButton"] > button:focus p {

        color: #FFFFFF !important;
    }


    /* =====================================================
       TARJETAS DE CARRERAS RECOMENDADAS
    ===================================================== */

    .resultado {

        padding: 22px;

        margin-top: 14px;

        margin-bottom: 18px;

        border:
            1px solid
            rgba(
                255,
                255,
                255,
                0.25
            );

        border-radius: 18px;

        background:
            rgba(
                15,
                35,
                60,
                0.78
            );

        box-shadow:
            0 8px 22px
            rgba(
                0,
                0,
                0,
                0.20
            );

        backdrop-filter:
            blur(5px);
    }


    /* =====================================================
       TITULO DE CADA CARRERA
    ===================================================== */

    .resultado h3 {

        color: white;

        font-size: 1.35rem;

        font-weight: 750;

        line-height: 1.3;

        margin-top: 0;

        margin-bottom: 12px;
    }


    /* =====================================================
       DESCRIPCION DE LA CARRERA
    ===================================================== */

    .resultado p {

        color: #E8F1F8;

        font-size: 1rem;

        line-height: 1.55;

        margin-top: 14px;

        margin-bottom: 0;
    }


    /* =====================================================
       ETIQUETA DE AFINIDAD
    ===================================================== */

    .afinidad-carrera {

        display: inline-block;

        color: white;

        background:
            rgba(
                47,
                128,
                237,
                0.35
            );

        border:
            1px solid
            rgba(
                120,
                190,
                255,
                0.45
            );

        border-radius: 999px;

        padding:
            7px 13px;

        font-size: 0.95rem;

        font-weight: 700;

        margin-top: 2px;
    }


    /* =====================================================
       TITULOS Y TEXTOS SOBRE EL FONDO
    ===================================================== */

    .stApp h1,
    .stApp h2,
    .stApp h3 {

        color: white;
    }


    .stApp p {

        color: white;
    }


    .stApp label {

        color: white;
    }


    /* =====================================================
       RADIO BUTTONS
    ===================================================== */

    div[data-testid="stRadio"] label {

        color: white;

        font-size: 1rem;
    }


    /* =====================================================
       INPUTS
    ===================================================== */

    div[data-baseweb="input"] input {

        font-size: 1rem;
    }


    /* =====================================================
       SELECTBOX
    ===================================================== */

    div[data-baseweb="select"] {

        font-size: 1rem;
    }


    /* =====================================================
       BARRA DE PROGRESO
    ===================================================== */

    div[data-testid="stProgress"] {

        margin-top: 8px;

        margin-bottom: 8px;
    }


    /* =====================================================
       IMAGENES
    ===================================================== */

    div[data-testid="stImage"] img {

        border-radius: 16px;
    }


    /* =====================================================
       DIVISORES
    ===================================================== */

    hr {

        border-color:
            rgba(
                255,
                255,
                255,
                0.25
            );
    }


    /* =====================================================
       MENSAJES DE ERROR
    ===================================================== */

    div[data-testid="stAlert"] {

        border-radius: 14px;
    }


    /* =====================================================
       CELULARES
    ===================================================== */

    @media (max-width: 600px) {

        .block-container {

            padding-left: 0.8rem;

            padding-right: 0.8rem;

            padding-bottom: 1.5rem;
        }


        .stButton > button {

            min-height: 52px;

            font-size: 1rem;
        }


        div[data-testid="stFormSubmitButton"] > button {

            min-height: 54px !important;

            font-size: 1rem !important;

            border-radius: 13px !important;
        }


        div[data-testid="stFormSubmitButton"] > button p {

            font-size: 1rem !important;
        }


        .resultado {

            padding: 17px;

            border-radius: 15px;

            margin-top: 12px;

            margin-bottom: 14px;
        }


        .resultado h3 {

            font-size: 1.15rem;

            line-height: 1.35;
        }


        .resultado p {

            font-size: 0.93rem;

            line-height: 1.5;
        }


        .afinidad-carrera {

            font-size: 0.88rem;

            padding:
                6px 10px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)
#=========================================================
#FONDO PARA DATOS, TEST Y RESULTADO
# ==========================================================

def poner_fondo():

    st.markdown(
        """
        <style>

        .stApp {
            background:
                linear-gradient(
                    rgba(0,0,0,0.30),
                    rgba(0,0,0,0.30)
                ),
                url("app/static/ies-n-11.webp");
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Usamos la imagen mediante CSS generado con archivo local.
    # Este segundo bloque es el que realmente coloca
    # la fotografía del instituto.

    import base64

    with open(RUTA_FOTO, "rb") as archivo:

        imagen_base64 = base64.b64encode(
            archivo.read()
        ).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background:
                linear-gradient(
                    rgba(0,0,0,0.30),
                    rgba(0,0,0,0.30)
                ),
                url(
                    "data:image/jpeg;base64,{imagen_base64}"
                );

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;

            min-height: 100vh;
        }}

        .stApp h1,
        .stApp h2,
        .stApp h3,
        .stApp p,
        .stApp label {{
            color: white;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# ESTILO EXCLUSIVO DE LA PANTALLA DE INICIO
# ==========================================================

def estilo_inicio():

    st.markdown(
        """
        <style>

        /* =================================================
           FONDO PRINCIPAL
        ================================================= */

        .stApp {

            background:

                radial-gradient(
                    circle at 15% 15%,
                    rgba(56, 189, 248, 0.16),
                    transparent 32%
                ),

                radial-gradient(
                    circle at 90% 80%,
                    rgba(45, 212, 191, 0.10),
                    transparent 30%
                ),

                linear-gradient(
                    145deg,
                    #102A43 0%,
                    #163A63 55%,
                    #102A43 100%
                );

            min-height: 100vh;
        }


        /* =================================================
           CONTENEDOR
        ================================================= */

        .block-container {

            max-width: 820px;

            margin-left: auto;
            margin-right: auto;

            padding-top: 1.7rem;

            padding-left: 1rem;
            padding-right: 1rem;

            padding-bottom: 3rem;
        }


        /* =================================================
           IDENTIDAD DEL IES
        ================================================= */

        .hero-kicker {

            text-align: center;

            font-size: 0.92rem;

            font-weight: 800;

            letter-spacing: 0.15rem;

            color: #7DD3FC;

            margin-top: 12px;

            margin-bottom: 14px;
        }


        /* =================================================
           TITULO
        ================================================= */

        .hero-title {

            text-align: center;

            color: #FFFFFF;

            font-size: 3.15rem;

            font-weight: 850;

            line-height: 1.05;

            margin-top: 5px;

            margin-bottom: 20px;
        }


        /* =================================================
           SUBTITULO
        ================================================= */

        .hero-subtitle {

            max-width: 680px;

            margin-left: auto;
            margin-right: auto;

            margin-bottom: 30px;

            text-align: center;

            color: #E8F3FA;

            font-size: 1.13rem;

            line-height: 1.55;
        }


        /* =================================================
           CHIPS DE AREAS
        ================================================= */

        .chips {

            display: flex;

            justify-content: center;

            align-items: center;

            flex-wrap: wrap;

            gap: 12px;

            margin-top: 16px;

            margin-bottom: 34px;
        }


        .chip {

            display: inline-flex;

            align-items: center;

            gap: 7px;

            border-radius: 999px;

            padding: 10px 17px;

            font-size: 0.96rem;

            font-weight: 750;

            border: 1px solid transparent;

            box-shadow:
                0 6px 16px
                rgba(0, 0, 0, 0.15);
        }


        /* TECNOLOGIA */

        .chip-tech {

            color: #E0F7FF;

            background:
                rgba(56, 189, 248, 0.22);

            border-color:
                rgba(56, 189, 248, 0.65);
        }


        /* SALUD */

        .chip-salud {

            color: #FFF1F3;

            background:
                rgba(251, 113, 133, 0.22);

            border-color:
                rgba(251, 113, 133, 0.70);
        }


        /* GASTRONOMIA */

        .chip-gastro {

            color: #FFF8DD;

            background:
                rgba(251, 191, 36, 0.22);

            border-color:
                rgba(251, 191, 36, 0.70);
        }


        /* TURISMO */

        .chip-turismo {

            color: #E8FFFA;

            background:
                rgba(45, 212, 191, 0.22);

            border-color:
                rgba(45, 212, 191, 0.70);
        }


        /* =================================================
           TARJETA CLARA DE INFORMACION
        ================================================= */

        .info-card {

            width: 100%;

            box-sizing: border-box;

            background:
                rgba(248, 250, 252, 0.96);

            border:
                1px solid
                rgba(255, 255, 255, 0.85);

            border-radius: 22px;

            padding: 26px 22px;

            margin-top: 8px;

            margin-bottom: 24px;

            box-shadow:
                0 12px 35px
                rgba(0, 0, 0, 0.22);
        }


        .info-grid {

            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 18px;

            text-align: center;

            align-items: stretch;
        }


        /* =================================================
           CADA BLOQUE DE INFORMACION
        ================================================= */

        .info-item {

            padding: 13px 10px;

            border-radius: 15px;

            color: #102A43;
        }


        .info-icon {

            display: block;

            font-size: 2rem;

            margin-bottom: 8px;
        }


        .info-item strong {

            display: block;

            color: #102A43;

            font-size: 1.08rem;

            font-weight: 800;

            margin-bottom: 6px;
        }


        .info-item span {

            display: block;

            color: #486581;

            font-size: 0.90rem;

            line-height: 1.4;
        }


        /* COLORES DE LOS TRES BLOQUES */

        .info-preguntas {

            background:
                rgba(56, 189, 248, 0.12);

            border-top:
                4px solid #38BDF8;
        }


        .info-tiempo {

            background:
                rgba(251, 191, 36, 0.13);

            border-top:
                4px solid #FBBF24;
        }


        .info-resultado {

            background:
                rgba(45, 212, 191, 0.13);

            border-top:
                4px solid #2DD4BF;
        }


        /* =================================================
           NOTA
        ================================================= */

        .nota {

            max-width: 680px;

            margin-left: auto;
            margin-right: auto;

            margin-top: 16px;
            margin-bottom: 24px;

            text-align: center;

            color: #D9EAF5;

            font-size: 0.92rem;

            line-height: 1.5;
        }


        /* =================================================
           BOTON COMENZAR
        ================================================= */

        .stButton > button {

            width: 100%;

            min-height: 60px;

            border-radius: 16px;

            border:
                1px solid
                rgba(255, 255, 255, 0.35);

            background:
                linear-gradient(
                    135deg,
                    #38BDF8,
                    #0EA5E9
                );

            color: #082F49;

            font-size: 1.08rem;

            font-weight: 850;

            box-shadow:
                0 9px 24px
                rgba(14, 165, 233, 0.30);

            transition:
                transform 0.15s ease,
                box-shadow 0.15s ease;
        }


        .stButton > button:hover {

            color: #082F49;

            border-color: #7DD3FC;

            transform: translateY(-2px);

            box-shadow:
                0 13px 28px
                rgba(14, 165, 233, 0.40);
        }


        /* =================================================
           IMAGEN INSTITUCIONAL
        ================================================= */

        div[data-testid="stImage"] img {

            border-radius: 18px;
        }


        /* =================================================
           CELULARES
        ================================================= */

        @media (max-width: 600px) {

            .block-container {

                padding-top: 1.1rem;

                padding-left: 0.85rem;
                padding-right: 0.85rem;

                padding-bottom: 2rem;
            }


            .hero-kicker {

                font-size: 0.72rem;

                letter-spacing: 0.08rem;
            }


            .hero-title {

                font-size: 2.15rem;

                margin-bottom: 15px;
            }


            .hero-subtitle {

                font-size: 0.98rem;

                margin-bottom: 22px;
            }


            .chips {

                gap: 8px;

                margin-bottom: 24px;
            }


            .chip {

                font-size: 0.83rem;

                padding: 8px 11px;
            }


            .info-card {

                padding: 15px;

                border-radius: 18px;
            }


            .info-grid {

                grid-template-columns: 1fr;

                gap: 10px;
            }


            .info-item {

                padding: 11px 9px;
            }


            .info-icon {

                font-size: 1.65rem;
            }


            .stButton > button {

                min-height: 56px;

                font-size: 1rem;
            }

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
# FONDO SEGÚN PANTALLA
# ==========================================================

if st.session_state.pagina == "inicio":

    estilo_inicio()

else:

    poner_fondo()
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
