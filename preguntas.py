import random

PREGUNTAS = [
    {
        "id": 1,
        "orientacion": "tecnologia",
        "pregunta": "Cuanto te interesa aprender a programar y crear aplicaciones?"
    },
    {
        "id": 2,
        "orientacion": "tecnologia",
        "pregunta": "Cuanto disfrutas resolver problemas utilizando computadoras o tecnologia?"
    },
    {
        "id": 3,
        "orientacion": "tecnologia",
        "pregunta": "Cuanto te interesa analizar informacion para encontrar patrones o soluciones?"
    },
    {
        "id": 4,
        "orientacion": "tecnologia",
        "pregunta": "Cuanto te atraen la Inteligencia Artificial, los datos y las nuevas tecnologias?"
    },
    {
        "id": 5,
        "orientacion": "gastronomia",
        "pregunta": "Cuanto te interesa preparar comidas y experimentar con ingredientes?"
    },
    {
        "id": 6,
        "orientacion": "gastronomia",
        "pregunta": "Cuanto te interesa conocer la gastronomia y cultura alimentaria de distintas regiones?"
    },
    {
        "id": 7,
        "orientacion": "gastronomia",
        "pregunta": "Cuanto disfrutas crear nuevas recetas o presentar alimentos de manera creativa?"
    },
    {
        "id": 8,
        "orientacion": "gastronomia",
        "pregunta": "Cuanto te gustaria trabajar en actividades relacionadas con cocina, alimentos o gastronomia regional?"
    },
    {
        "id": 9,
        "orientacion": "salud",
        "pregunta": "Cuanto te interesa aprender sobre el cuidado y la prevencion de la salud?"
    },
    {
        "id": 10,
        "orientacion": "salud",
        "pregunta": "Cuanto te gustaria ayudar a otras personas en situaciones relacionadas con su bienestar?"
    },
    {
        "id": 11,
        "orientacion": "salud",
        "pregunta": "Cuanto interes tenes por la ciencia aplicada al cuerpo humano, la prevencion o el laboratorio?"
    },
    {
        "id": 12,
        "orientacion": "salud",
        "pregunta": "Cuanto te interesa participar en acciones de promocion, prevencion y cuidado de la salud?"
    },
    {
        "id": 13,
        "orientacion": "turismo",
        "pregunta": "Cuanto te interesa conocer lugares, culturas y atractivos turisticos?"
    },
    {
        "id": 14,
        "orientacion": "turismo",
        "pregunta": "Cuanto te interesa organizar actividades para visitantes y viajeros?"
    },
    {
        "id": 15,
        "orientacion": "turismo",
        "pregunta": "Cuanto te gusta comunicarte con personas de diferentes lugares y culturas?"
    },
    {
        "id": 16,
        "orientacion": "turismo",
        "pregunta": "Cuanto te interesa la atencion al visitante, la hospitalidad y la organizacion de servicios?"
    }
]


def obtener_preguntas_mezcladas():
    preguntas = PREGUNTAS.copy()
    random.shuffle(preguntas)
    return preguntas