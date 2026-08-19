import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ==========================================
# PEGA AQUÍ LA URL DE TU GOOGLE SHEET
# ==========================================
URL_GOOGLE_SHEET = "https://docs.google.com/spreadsheets/d/1Gf78RUz3HEKdQxbwYL0pa4fEFEyw-9zMzY-iqoaTx8c/edit?usp=sharing"
def enviar_correo_resultado(email_destino, nombre, carrera_principal, descripcion_carrera):
    try:
        # Recupera las credenciales de Streamlit
        remitente = st.secrets["email"]["direccion"]
        password = st.secrets["email"]["password"]

        # Configuración del mensaje
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = email_destino
        msg['Subject'] = "Resultados de tu Test Vocacional - IES N.º 11"

        # Cuerpo del correo electrónico
        cuerpo = f"""
        ¡Hola {nombre}!
        
        Gracias por visitar el stand del IES N.º 11 en la exposición.
        
        Según tus respuestas en el test vocacional, la tecnicatura con mayor afinidad para vos es:
        
        🎓 {carrera_principal}
        
        ¿De qué se trata?
        {descripcion_carrera}
        
        ¡Te esperamos en nuestra institución para que comiences tu camino profesional!
        
        Saludos,
        El equipo del IES N.º 11
        """
        
        msg.attach(MIMEText(cuerpo, 'plain'))

        # Conexión al servidor de Gmail y envío
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.send_message(msg)
        server.quit()
        
    except Exception as e:
        print(f"No se pudo enviar el correo: {e}")
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
        # 4. Abrir la hoja y agregar la fila
        hoja = cliente.open_by_url(URL_GOOGLE_SHEET).sheet1
        hoja.append_row(fila)
        
        # 5. ENVIAR EL CORREO AUTOMÁTICO
        carrera_recomendada = resultado["top4"][0]["carrera"]
        descripcion = resultado["top4"][0]["descripcion"]
        
        enviar_correo_resultado(email, nombre, carrera_recomendada, descripcion)
        
        # Retorna la cantidad de filas para usarlo como "Número de Registro"
        return len(hoja.get_all_values())
        
        # Retorna la cantidad de filas para usarlo como "Número de Registro"
        return len(hoja.get_all_values())
        
    except Exception as e:
        # Enviar el error a la pantalla de Streamlit para poder leerlo
        st.error(f"Error de conexión con Google Sheets: {e}")
        return 9999
