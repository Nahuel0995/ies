import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ==========================================
# PEGA AQUÍ LA URL DE TU GOOGLE SHEET
# ==========================================
URL_GOOGLE_SHEET = "https://docs.google.com/spreadsheets/d/1Gf78RUz3HEKdQxbwYL0pa4fEFEyw-9zMzY-iqoaTx8c/edit?usp=sharing"

def guardar_resultado(nombre, apellido, email, edad, sexo, respuestas, resultado):
    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. Armamos la fila con los datos principales en una lista
    fila = [
        fecha, 
        nombre, 
        apellido, 
        email, 
        edad, 
        sexo,
        resultado["tipo_perfil"],
        resultado["perfil_principal"][0], 
        resultado["perfil_principal"][1],
        resultado["perfil_secundario"][0], 
        resultado["perfil_secundario"][1],
        resultado["top4"][0]["carrera"], 
        resultado["top4"][0]["afinidad"],
        resultado["top4"][1]["carrera"], 
        resultado["top4"][1]["afinidad"],
        resultado["top4"][2]["carrera"], 
        resultado["top4"][2]["afinidad"],
        resultado["top4"][3]["carrera"], 
        resultado["top4"][3]["afinidad"]
    ]

    # 2. Agregamos las 16 respuestas al final de la fila
    for numero in range(1, 17):
        fila.append(respuestas.get(numero, ""))

    try:
        # 3. Conectar a Google Sheets usando los "Secrets" de Streamlit
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
        ]
        
        # Lee las credenciales ocultas en la nube de Streamlit
        credenciales = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=scopes
        )
        
        cliente = gspread.authorize(credenciales)
        
        # 4. Abrir la hoja y agregar la fila
        hoja = cliente.open_by_url(URL_GOOGLE_SHEET).sheet1
        hoja.append_row(fila)
        
        # Retorna la cantidad de filas para usarlo como "Número de Registro"
        return len(hoja.get_all_values())
        
    except Exception as e:
        # Enviar el error a la pantalla de Streamlit para poder leerlo
        st.error(f"Error de conexión con Google Sheets: {e}")
        return 9999
