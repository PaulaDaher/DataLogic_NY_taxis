import streamlit as st
from PIL import Image
import pandas as pd
import streamlit.components.v1 as components

# Título e ícono de la página
st.set_page_config(page_title='DashBoard', page_icon='✨', layout='wide')

# Header
with st.container():
    st.markdown("<h1 style='text-align: center;'>Visualización de datos</h1>", unsafe_allow_html=True)

# Dashboard
embed_code = """
<iframe title="Dashboard_NY_taxis" width="1280" height="720" src="https://app.powerbi.com/view?r=eyJrIjoiYjFiY2RlNjYtZGFjZC00YmJmLTlmOGYtMWQ2ZWYyMWUxYTMxIiwidCI6IjJhMTY3ZDI3LTBhMmEtNGM0MC04N2I5LTY4ZjQzODA5MDQ3MiJ9" frameborder="0" allowFullScreen="true"></iframe>
"""

# Usar st.components.v1.html para renderizar el iframe
components.html(embed_code, width=1280, height=720)