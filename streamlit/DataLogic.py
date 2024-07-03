import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# Título e ícono de la página
st.set_page_config(page_title='DataLogic', page_icon='🚕', layout='wide')

with st.container():
    portada = Image.open('./streamlit/images/datalogic_banner.png')
    st.image(portada, use_column_width=True)

# Presentación
with st.container():
    # st.markdown("<h1 style='text-align: center;'>Somos Data Logic</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Creamos soluciones para aumentar los ingresos de tu empresa</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Somos apasionados por la tecnología y la innovación, especializados en la extracción y procesamiento de datos para su análisis</p>", unsafe_allow_html=True)

# Servicios
with st.container():
    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("## **Nuestros Servicios**", unsafe_allow_html=True)
        st.markdown("- 🔍 **Extracción de Datos**: Recopilamos información valiosa de diversas fuentes de manera eficiente.")
        st.markdown("- 📊 **Análisis de Datos**: Transformamos tus datos en insights accionables.")
        st.markdown("- 📈 **Visualización de Datos**: Creamos dashboards interactivos y visualizaciones personalizadas.")
        st.markdown("- 🔮 **Modelos predictivos**: Desarrollamos e implementamos modelos predictivos para ayudar en tus decisiones futuras.")
        # st.markdown("- **Consultoría en Tecnología**: Asesoramiento en la implementación de soluciones tecnológicas.")

    with col2:
        imagen_servicios = Image.open('./streamlit/images/analisis.png')
        st.image(imagen_servicios, width=280)

# Por qué elegirnos
with st.container():
    col3, col4 = st.columns([2,1])

    with col1:
        st.header("¿Por qué elegir Data Logic?")
        st.markdown("""
        - 💡 Enfoque personalizado para cada cliente
        - 🔬 Uso de tecnologías de vanguardia
        - 🤝 Compromiso con el éxito de nuestros clientes
        """)
    
    with col2:
        imagen_elegir = Image.open('./streamlit/images/inteligencia.png')
        st.image(imagen_elegir, width=200)

# Contacto equipo
with st.container():
    st.header('Equipo de trabajo')

    # Datos de los miembros del equipo
    miembros = [
        {"nombre": "Mateo Tagliaferro", "imagen": "./streamlit/images/mateo.png", "linkedin": "https://www.linkedin.com/in/mateo-tagliaferro-49702a268/", "rol": "Data Scientist", "email": "mateo@datalogic.com"},
        {"nombre": "Santos Iparraguirre", "imagen": "./streamlit/images/santos.png", "linkedin": "https://www.linkedin.com/in/santos-iparraguirre-b738a82b3/", "rol": "Data Engineer", "email": "santos@datalogic.com"},
        {"nombre": "Paula Daher", "imagen": "./streamlit/images/pau.png", "linkedin": "https://www.linkedin.com/in/poldajer/", "rol": "Data Analyst", "email": "paula@datalogic.com"},
        {"nombre": "Juan Carlos Garzón Rodriguez", "imagen": "./streamlit/images/juan.png", "linkedin": "https://www.linkedin.com/in/miembro4", "rol": "Data Scientist", "email": "juan@datalogic.com"},
        {"nombre": "Jesús Felipe Sepulveda", "imagen": "./streamlit/images/felipe.png", "linkedin": "https://www.linkedin.com/in/jesus-felipe-sepulveda-alvarez-21684a115/", "rol": "Data Analyst", "email": "felipe@datalogic.com"}
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