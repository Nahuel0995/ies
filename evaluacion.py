from carreras import CARRERAS


ORIENTACIONES = {

    "tecnologia": {

        "nombre": "💻 Analítico-Tecnológico",

        "descripcion":
        "Interés por tecnología, análisis, programación, "
        "innovación y resolución de problemas."
    },


    "gastronomia": {

        "nombre": "🍳 Creativo-Gastronómico",

        "descripcion":
        "Interés por cocina, creatividad, alimentos, "
        "cultura y experiencias gastronómicas."
    },


    "salud": {

        "nombre": "🏥 Científico-Asistencial",

        "descripcion":
        "Interés por salud, cuidado, prevención, "
        "investigación y bienestar de las personas."
    },


    "turismo": {

        "nombre": "🌎 Social-Comunicativo",

        "descripcion":
        "Interés por personas, comunicación, viajes, "
        "cultura, organización y hospitalidad."
    }
}


def calcular_orientaciones(
    respuestas,
    preguntas
):

    puntajes = {
        "tecnologia": 0,
        "gastronomia": 0,
        "salud": 0,
        "turismo": 0
    }


    cantidades = {
        "tecnologia": 0,
        "gastronomia": 0,
        "salud": 0,
        "turismo": 0
    }


    for pregunta in preguntas:

        orientacion = pregunta["orientacion"]

        respuesta = respuestas.get(
            pregunta["id"],
            0
        )


        puntajes[orientacion] += respuesta

        cantidades[orientacion] += 1


    porcentajes = {}


    for orientacion in puntajes:

        maximo = cantidades[orientacion] * 5

        porcentajes[orientacion] = round(
            (puntajes[orientacion] / maximo) * 100,
            2
        )


    return puntajes, porcentajes


def determinar_tipo_perfil(
    ranking
):

    valores = [
        valor
        for _, valor in ranking
    ]


    diferencia_total = (
        max(valores) -
        min(valores)
    )


    if diferencia_total <= 15:

        return "explorador"


    diferencia = (
        ranking[0][1] -
        ranking[1][1]
    )


    if diferencia < 10:

        return "combinado"


    return "definido"


def calcular_afinidad_carreras(
    porcentajes
):

    resultados = []


    for carrera, datos in CARRERAS.items():

        puntaje = 0

        peso_total = 0


        for orientacion in porcentajes:

            peso = datos[orientacion]


            puntaje += (
                porcentajes[orientacion]
                * peso
            )


            peso_total += peso


        afinidad = (
            puntaje / peso_total
            if peso_total > 0
            else 0
        )


        resultados.append({

            "carrera": carrera,

            "afinidad": round(
                afinidad,
                2
            ),

            "descripcion":
                datos["descripcion"],
            "plan_estudio": datos.get("plan_estudio", "No disponible")
        })


    resultados.sort(

        key=lambda x: x["afinidad"],

        reverse=True
    )


    return resultados


def obtener_resultado(
    respuestas,
    preguntas
):

    puntajes, porcentajes = (
        calcular_orientaciones(
            respuestas,
            preguntas
        )
    )


    ranking = sorted(

        porcentajes.items(),

        key=lambda x: x[1],

        reverse=True
    )


    carreras = (
        calcular_afinidad_carreras(
            porcentajes
        )
    )


    return {

        "puntajes": puntajes,

        "porcentajes": porcentajes,

        "ranking_orientaciones":
            ranking,

        "tipo_perfil":
            determinar_tipo_perfil(
                ranking
            ),

        "perfil_principal":
            ranking[0],

        "perfil_secundario":
            ranking[1],

        "carreras":
            carreras,

        "top4":
            carreras[:4]
    }
