import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Menú')

# Diccionario con las imágenes y sus nombres
images = {
    "Objetivos": "./images/img_objetivos.png",
    "Alcances": "./images/alcances.png",
    "Fuentes": "./images/fuentes.png",
    "Arquitecturas-Tecnologias": "./images/arquitectura(2).png",
    "Metodología del Trabajo - SCRUM": "./images/gantt(1).png"
}

# Crear botones para cada imagen
selected_image = None
for image_name in images.keys():
    if st.button(image_name):
        selected_image = images[image_name]

# Mostrar la imagen seleccionada
if selected_image:
    st.image(selected_image, caption=image_name)
