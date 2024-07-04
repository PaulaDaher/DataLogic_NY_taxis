import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título e ícono de la página
st.set_page_config(page_title='Predicción', page_icon='📈', layout='wide')

# Función para cargar los datos
@st.cache_data
def load_future_predictions():
    return pd.read_csv('./streamlit/datasets/modelo_arima.csv')

@st.cache_data
def load_historical_data():
    return pd.read_csv('./streamlit/datasets/base_arima.csv', index_col=0, parse_dates=True)

# Cargar los datos
future_predictions = load_future_predictions()
df = load_historical_data()

# Obtener los meses inicial y final
start_month = df.index[-1].strftime('%B %Y')
end_month = pd.date_range(start=df.index[-1], periods=180, freq='D')[-1].strftime('%B %Y')

# Configurar la página de Streamlit
st.markdown("<h1 style='text-align: center;'>Predicción de la demanda de taxis en New York</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Periodo: Mayo de 2024 - Noviembre 2024</h3>", unsafe_allow_html=True)

# Visualizar las predicciones futuras
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(df, label='Histórico')
ax.plot(pd.date_range(start=df.index[-1], periods=180, freq='D'), future_predictions, label='Predicciones Futuras', color='green')
ax.set_xlabel('Fecha')
ax.set_ylabel('Cantidad de Viajes')
#ax.set_title(f'Predicciones Futuras de Cantidad de Viajes desde {start_month} hasta {end_month}')
ax.legend()

# Mostrar la gráfica en Streamlit
st.pyplot(fig)

