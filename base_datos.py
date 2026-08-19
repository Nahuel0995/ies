from pathlib import Path
from datetime import datetime

import pandas as pd


ARCHIVO = Path(
    "resultados_test.xlsx"
)


def guardar_resultado(

    nombre,
    apellido,
    email,
    edad,
    sexo,
    respuestas,
    resultado

):

    fecha = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    registro = {

        "Fecha": fecha,

        "Nombre": nombre,

        "Apellido": apellido,
        "Email": email,

        "Edad": edad,

        "Sexo": sexo,

        "Tipo_Perfil":
            resultado["tipo_perfil"],

        "Orientacion_Principal":
            resultado["perfil_principal"][0],

        "Porcentaje_Principal":
            resultado["perfil_principal"][1],

        "Orientacion_Secundaria":
            resultado["perfil_secundario"][0],

        "Porcentaje_Secundaria":
            resultado["perfil_secundario"][1],

        "Carrera_1":
            resultado["top4"][0]["carrera"],

        "Afinidad_1":
            resultado["top4"][0]["afinidad"],

        "Carrera_2":
            resultado["top4"][1]["carrera"],

        "Afinidad_2":
            resultado["top4"][1]["afinidad"],

        "Carrera_3":
            resultado["top4"][2]["carrera"],

        "Afinidad_3":
            resultado["top4"][2]["afinidad"],

        "Carrera_4":
            resultado["top4"][3]["carrera"],

        "Afinidad_4":
            resultado["top4"][3]["afinidad"]
    }


    # Guardar las 16 respuestas

    for numero in range(1, 17):

        registro[
            f"Pregunta_{numero}"
        ] = respuestas.get(
            numero,
            ""
        )


    # ---------------------------------
    # Si ya existe el Excel
    # ---------------------------------

    if ARCHIVO.exists():

        try:

            anterior = pd.read_excel(
                ARCHIVO
            )


            nuevo = pd.DataFrame(
                [registro]
            )


            df = pd.concat(
                [
                    anterior,
                    nuevo
                ],
                ignore_index=True
            )


        except Exception:

            df = pd.DataFrame(
                [registro]
            )


    else:

        df = pd.DataFrame(
            [registro]
        )


    df.to_excel(
        ARCHIVO,
        index=False
    )


    return len(df)