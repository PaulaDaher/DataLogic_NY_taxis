import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# Título e ícono de la página
st.set_page_config(page_title='Proyecto', page_icon='📋', layout='wide')

# Título de la aplicación
st.markdown("<h1 style='text-align: center;'>Visión General del Proyecto</h1>", unsafe_allow_html=True)

# Diccionario con las imágenes y sus nombres
images = {
    "Objetivos": "./streamlit/images/img_objetivos.png",
    "Alcances": "./streamlit/images/alcances.png",
    "Fuentes": "./streamlit/images/fuentes.png",
    "Arquitectura": "./streamlit/images/Arquitectura.png",
    "Metodología SCRUM": "./streamlit/images/Scrum.png"
}

# Crear columnas para los botones
columns = st.columns(len(images))

# Crear botones para cada imagen en columnas
selected_image = None
for col, (image_name, image_path) in zip(columns, images.items()):
    if col.button(image_name):
        selected_image = image_path

# Mostrar la imagen seleccionada
if selected_image:
    st.image(selected_image, caption=image_name)
