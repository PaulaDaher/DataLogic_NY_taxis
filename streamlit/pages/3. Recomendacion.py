import pandas as pd
import streamlit as st

# Cargar datos
autos_electricos = pd.read_csv("./datasets/df_electric_cars.csv")

# Renombrar columnas
renombrar_columnas = {
    "Brand": "Marca",
    "ROI": "ROI (%)",
    "price_dollars": "Costo Unitario",
    "Combined (wh/km)": "Eficiencia (Wh/Km)",
    "range_km": "Distancia antes de cargar (Km)",
    "battery_life_km": "Vida útil batería (Km)",
    "Model": "Modelo",
    "model_year": "Año salida",
    "vehicle_class": "Clase vehiculo",
    "charge_time_minutes": "Tiempo de carga (min)",
    "engine_size_L": "Tamaño motor (Litros)",
    "engine_cylinder": "Cilindros motor",
    "transmission_type": "Tipo de trasmisión"
}
autos_electricos = autos_electricos.rename(columns=renombrar_columnas)

# Obtener marcas ordenadas
marcas_ordenadas = sorted(autos_electricos['Marca'].unique())

# Configuración de la página de Streamlit
st.set_page_config(page_title="Recomendación de Taxis Eléctricos para la ciudad de New York", page_icon="-", layout="wide")

with st.container():
    st.title("Recomendación de Taxis Eléctricos")
    st.write("Este es un prototipo de recomendación de taxis eléctricos en la Ciudad de Nueva York.")

    # Cuadro de texto para seleccionar la cantidad de taxis (opcional)
    cantidad_taxis = st.number_input('Cantidad de Taxis a Consultar', min_value=1, max_value=2000, value=1)

    # Seleccionar una marca
    seleccionada = st.selectbox('Selecciona una Marca', options=marcas_ordenadas)

    # Botón para validar y realizar la consulta
    if st.button('Consultar'):
        if seleccionada and cantidad_taxis >= 1:
            # Filtrar dataframe según la marca seleccionada
            df_filtrado = autos_electricos[autos_electricos['Marca'] == seleccionada].copy()
            df_filtrado["Inversión"] = df_filtrado["Costo Unitario"] * cantidad_taxis

            # Calculo de ROI
            distancia_promedio_por_viaje_en_km = 7.41
            distancia_promedio_recorrida_en_un_año_por_taxi = distancia_promedio_por_viaje_en_km * 21 * 365
            df_filtrado["Consumo promedio kWh"] = df_filtrado["Eficiencia (Wh/Km)"] / 1000 * distancia_promedio_recorrida_en_un_año_por_taxi
            precio_kilowatts_por_hora_Manhattan = 0.241
            eficiencia_de_carga_vehiculo_electrico = 0.8
            df_filtrado["Costo de Carga"] = df_filtrado["Consumo promedio kWh"] / eficiencia_de_carga_vehiculo_electrico * precio_kilowatts_por_hora_Manhattan
            conductores = 3
            promedio_viajes_futuros_por_taxi = 7 * conductores
            promedio_ingreso_por_viaje = 30
            dias_laborables = 365
            seguro = 5304
            sueldos = 55000 * conductores * cantidad_taxis
            ingresos_totales_anuales = promedio_viajes_futuros_por_taxi * cantidad_taxis * promedio_ingreso_por_viaje * dias_laborables
            costo_mtto_anual_promedio = 490 * cantidad_taxis
            df_filtrado["Costos Generales"] = df_filtrado["Costo Unitario"] * cantidad_taxis + df_filtrado["Costo de Carga"] * cantidad_taxis + seguro + sueldos + costo_mtto_anual_promedio
            roi = round((ingresos_totales_anuales - df_filtrado["Costos Generales"]) / df_filtrado["Costos Generales"] * 100, 2)

            df_filtrado["ROI (%)"] = roi

            # Formatos de Columnas
            df_filtrado['Inversión'] = df_filtrado['Inversión'].apply(lambda x: f"${x:,.0f}")
            df_filtrado['Costo Unitario'] = df_filtrado['Costo Unitario'].apply(lambda x: f"${x:,.0f}")
            df_filtrado['ROI (%)'] = df_filtrado['ROI (%)'].apply(lambda x: f"{x:.2%}")

            # Reordenar columnas para mostrar y excluir 'Marca'
            columnas_reordenadas = ['Modelo', 'Costo Unitario', 'Inversión', 'ROI (%)'] + [col for col in df_filtrado.columns if col not in ['Modelo', 'Costo Unitario', 'Inversión',  'ROI (%)']]
            df_reordenado = df_filtrado[columnas_reordenadas]
            df_reordenado = df_reordenado.drop(columns=['Marca'])

            # Mostrar la tabla con los modelos y columnas relacionadas
            st.write(f"Modelos de {seleccionada}:")
            st.table(df_reordenado)
        else:
            st.write('Por favor, selecciona una marca y/o cantidad.')
