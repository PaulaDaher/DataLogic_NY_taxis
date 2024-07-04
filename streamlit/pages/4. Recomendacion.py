import pandas as pd
import streamlit as st

# Cargar datos
autos_electricos = pd.read_csv("./streamlit/datasets/df_electric_cars_reco.csv")

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

# Obtener marcas ordenadas y agregar opción <Todas>
marcas_ordenadas = ['Todas'] + sorted(autos_electricos['Marca'].unique())

# Configuración de la página de Streamlit
st.set_page_config(page_title="Recomendación", page_icon="🚕", layout="wide")

with st.container():
    st.title("Recomendación de modelos de autos")
    st.markdown("<h3>Este es un sistema de recomendación de modelos de autos eléctricos para la implementación de una flota de taxis.</h3>", unsafe_allow_html=True)
    st.markdown("""
                A continuación ingrese la cantidad de autos que desea tener en su flota de taxis y su marca de preferencia.  
                Como respuesta obtendrá recomendaciones sobre modelos en los cuales invertir, información sobre sus costos y un retorno de la inversión a realizar.""")
    
    st.markdown("<br></br>", unsafe_allow_html=True)

    # Cuadro de texto para seleccionar la cantidad de taxis (opcional)
    cantidad_taxis = st.number_input('**Cantidad de Taxis a adquirir**', min_value=1, max_value=2000, value=1)

    # Seleccionar una marca
    seleccionada = st.selectbox('**Selecciona una Marca**', options=marcas_ordenadas)

    # Botón para validar y realizar la consulta
    if st.button('Consultar'):
        if seleccionada and cantidad_taxis >= 1:
            # Filtrar dataframe según la marca seleccionada o todas
            if seleccionada == 'Todas':
                df_filtrado = autos_electricos.copy()
            else:
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
            df_filtrado['Costos Generales'] = df_filtrado['Costos Generales'].apply(lambda x: f"${x:,.0f}")
            df_filtrado['ROI (%)'] = df_filtrado['ROI (%)'].apply(lambda x: f"{x:.2%}")

            # Reordenar columnas para mostrar y excluir las no deseadas
            columnas_reordenadas = ['Marca', 'Modelo', 'Clase vehiculo', 'Costo Unitario', 'Costos Generales', 'Inversión', 'ROI (%)']

            df_reordenado = df_filtrado[columnas_reordenadas]

            # Ordenar el DataFrame por la columna 'ROI (%)' de menor a mayor
            df_reordenado = df_reordenado.sort_values(by='ROI (%)')

            # Aplicar estilos para centrar y poner en negrita los títulos de las columnas
            df_reordenado_styled = df_reordenado.style.set_properties(**{
                'text-align': 'center',
            }).set_table_styles([{
                'selector': 'th',
                'props': [('font-weight', 'bold'), ('text-align', 'center')]
            }])

            # Mostrar la tabla con estilos aplicados
            st.write(f"Modelos de {seleccionada}:")
            st.dataframe(df_reordenado_styled)

            # Mostrar la tabla con estilos aplicados
            #st.write(f"Modelos de {seleccionada}:")
            
    else:
        st.write('Por favor, selecciona una marca y/o cantidad.')