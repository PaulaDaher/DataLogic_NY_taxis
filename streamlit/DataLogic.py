import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# Título e ícono de la página
st.set_page_config(page_title='DataLogic', page_icon='💼', layout='wide')

with st.container():
    portada = Image.open('./streamlit/images/datalogic_banner.png')
    st.image(portada, use_column_width=True)

# Presentación
with st.container():
    st.markdown("<h2 style='text-align: center;'>Creamos herramientas de inteligencia de negocios para aplicar a tu empresa</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Somos apasionados por la tecnología y la innovación. Nos especializados en proyectos de Ciencia de Datos.</p>", unsafe_allow_html=True)

# Servicios
with st.container():

    st.markdown("## **Nuestros Servicios**", unsafe_allow_html=True)
    st.markdown("- 🔍 **Extracción de Datos**: Recopilamos información valiosa de diversas fuentes de manera eficiente.")
    st.markdown("- 📊 **Análisis de Datos**: Transformamos tus datos en insights accionables.")
    st.markdown("- 📈 **Visualización de Datos**: Creamos dashboards interactivos y visualizaciones personalizadas.")
    st.markdown("- 🤖 **Modelos de Machine Learning**: Desarrollamos e implementamos modelos de aprendizaje automático para ayudar en tus decisiones futuras.")

# Por qué elegirnos
with st.container():

 
    st.header("¿Por qué elegir Data Logic?")
    st.markdown("""
        - 💡 Enfoque personalizado para cada cliente
        - 🔬 Uso de tecnologías de vanguardia
        - 🤝 Compromiso con el éxito de nuestros clientes
        """)

# Contacto equipo
with st.container():
    st.header('Equipo de trabajo')

    # Datos de los miembros del equipo
    miembros = [
        {"nombre": "Jesús Felipe Sepulveda", "imagen": "./streamlit/images/felipe.png", "linkedin": "https://www.linkedin.com/in/jesus-felipe-sepulveda-alvarez-21684a115/", "rol": "Data Analyst", "email": "jhesuafelipe24@gmail.com"},
        {"nombre": "Paula Daher", "imagen": "./streamlit/images/pau.png", "linkedin": "https://www.linkedin.com/in/poldajer/", "rol": "Data Analyst", "email": "pauladaher050@gmail.com"},
        {"nombre": "Santos Iparraguirre", "imagen": "./streamlit/images/santos.png", "linkedin": "https://www.linkedin.com/in/santos-iparraguirre-b738a82b3/", "rol": "Data Engineer", "email": "santosiparraguirrem@gmail.com"},
        {"nombre": "Mateo Tagliaferro", "imagen": "./streamlit/images/mateo.png", "linkedin": "https://www.linkedin.com/in/mateo-tagliaferro-49702a268/", "rol": "Data Scientist", "email": "mateotagliaferro9@gmail.com"},
        {"nombre": "Juan Carlos Garzón Rodriguez", "imagen": "./streamlit/images/juan.png", "linkedin": "https://linkedin.com/in/juan-carlos-garzón-rodriguez-94457460 ", "rol": "Data Scientist", "email": " juankgarzon1@gmail.com"}
    ]

    cols = st.columns(5)  # Crear 5 columnas

    for col, miembro in zip(cols, miembros):
        with col:
            imagen = Image.open(miembro["imagen"])
            st.image(imagen, use_column_width=True)
            st.markdown(f"<p style='text-align: center;'><strong>{miembro['nombre']}</strong></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center;'>{miembro['rol']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center;'><a href='{miembro['linkedin']}' target='_blank'>LinkedIn</a></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center;'><a href='mailto:{miembro['email']}'>{miembro['email']}</a></p>", unsafe_allow_html=True)