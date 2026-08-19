from preguntas import PREGUNTAS

from evaluacion import (
    obtener_resultado,
    ORIENTACIONES
)


def crear_respuestas(
    tecnologia,
    gastronomia,
    salud,
    turismo
):

    valores = {

        "tecnologia":
            tecnologia,

        "gastronomia":
            gastronomia,

        "salud":
            salud,

        "turismo":
            turismo
    }


    return {

        pregunta["id"]:
            valores[
                pregunta["orientacion"]
            ]

        for pregunta in PREGUNTAS
    }


def probar_perfil(

    nombre,

    tecnologia,

    gastronomia,

    salud,

    turismo
):

    respuestas = crear_respuestas(

        tecnologia,

        gastronomia,

        salud,

        turismo
    )


    resultado = obtener_resultado(

        respuestas,

        PREGUNTAS
    )


    print()
    print("=" * 70)

    print(
        f"PERFIL: {nombre}"
    )

    print("=" * 70)


    for (

        orientacion,

        porcentaje

    ) in resultado[
        "ranking_orientaciones"
    ]:

        print(

            f"{ORIENTACIONES[orientacion]['nombre']}: "
            f"{porcentaje:.0f}%"
        )


    print(
        f"\nTipo de perfil: "
        f"{resultado['tipo_perfil']}"
    )


    print(
        "\nTOP 4 TECNICATURAS:"
    )


    for (

        posicion,

        carrera

    ) in enumerate(

        resultado["top4"],

        start=1
    ):

        print(

            f"{posicion}. "
            f"{carrera['carrera']} "
            f"→ "
            f"{carrera['afinidad']:.1f}%"
        )


# ==========================================================
# PRUEBAS
# ==========================================================


probar_perfil(

    "TECNOLÓGICO",

    5, 2, 2, 2
)


probar_perfil(

    "SALUD",

    2, 2, 5, 2
)


probar_perfil(

    "GASTRONÓMICO",

    2, 5, 2, 3
)


probar_perfil(

    "TURISMO",

    2, 3, 2, 5
)


probar_perfil(

    "TECNOLOGÍA + SALUD",

    5, 2, 5, 2
)


probar_perfil(

    "EXPLORADOR",

    4, 4, 4, 4
)