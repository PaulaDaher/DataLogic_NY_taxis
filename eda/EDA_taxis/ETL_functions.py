
# Todas las funciones que los taxis necesitan, sin necesidad de un merge. 
#  Función para filtrar el dataset de taxis
def filtrar_datasets(taxis):
    """
    Le pasamos cómo parametro el dataset de los taxis, cualquiera de los historicos, y lo que hace esta función es:
    1. Filtra un dataset cargado dentro de la misma función para dejar unicamente las zonas dentro del distrito de Manhattan.
    2. Filtra el dataset de los taxis por aquellas zonas correspondientes a Manhattan
    """
    try: 
        # 1
        # Importación de pandas necesria para trabajar los archivos
        import pandas as pd

        # Variables necesarias
        ruta_al_archivo_zonas = "../Datasets/taxi+_zone_lookup.csv"

        # Lectura del archivo que contiene todas las zonas de los taxis en la ciudad de Nueva York
        zonas = pd.read_csv(ruta_al_archivo_zonas)

        # Filtrado del dataframe recientemente cargado para dejar unicamente las zonas dentro del distrito de Manhattan
        # Este mismo dataset (Manhattan), posteriormente hay que subirlo a la nube
        Manhattan = zonas[zonas["Borough"] == "Manhattan"].drop("Borough",axis=1)

        # 2
        # Filtrado del dataframe de taxis ingresado a la función por aquellas zonas en dónde tanto la ID de la zona de subida cómo la ID de la zona de bajada corresponda con una ID de Manhattan. Esto sirve para quedarnos exclusivamente con la parte de los registros de los Taxis ocurrido en Manhattan, de ahí el nombre de la variable.
        movimientos_taxis_Manhattan = taxis[(taxis["PULocationID"].isin(Manhattan["LocationID"])) & (taxis["DOLocationID"].isin(Manhattan["LocationID"]))]

        # Impresión en pantalla de la cantidad de filas original y del porcentaje de reducción luego del filtrado, redondeado a dos decimales
        print(f"Originalmente el dataset tenía {len(taxis.index)} filas. \nLuego del filtrado por viajes en Manhattan se redujo un {round(100 - (len(movimientos_taxis_Manhattan.index) * 100 / len(taxis.index)), 2)}%")

        # Devolvemos el dataset filtrado.
        return movimientos_taxis_Manhattan
    except Exception as e:
        print(e)
    


# Función para normalizar las columnas y eliminar las no relevantes
def eliminar_columnas_no_relevantes(dataframe):
    """
    Lo que hace esta función es tomar un dataframe ingresado a la misma, y trabajar a partir de él con los siguientes pasos:
    1. Crea una variable local acordada previamente por el equipo de Data Logic de aquellas columnas que consideramos relevantes para nuestro análisis.
    2. Noramliza los nombres de las columnas del dataframe ingresado, pasandolas todas a mínusculas
    3. Normaliza los nombres de las columnas de la lista de columnas importantes, haciendolas todas mínusculas.
    4. Crea una nueva lista llamada columnas a eliminar teniendo en cuenta aquellas que no están en la lista de columnas importantes.
    5. Elimina las columnas no relevantes del dataframe.
    """
    try:
        
        # 1
        # Lista acordada por el equipo en dónde están las columnas que consideramos relevantes
        lista_columnas_importantes = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'trip_distance', 'PULocationID', 'DOLocationID', 'total_amount', 'passenger_count', 'payment_type']
        
        # 2
        # Normalizamos las columnas del DataFrame a minúsculas
        dataframe.columns = [col.lower() for col in dataframe.columns]

        # 3
        # Normalizamos la lista de columnas relevantes a minúsculas
        lista_columnas_importantes = [col.lower() for col in lista_columnas_importantes]
        
        # 4
        # Hacemos una lista con las columnas que no son relevantes
        columnas_a_eliminar = [col for col in dataframe.columns if col not in lista_columnas_importantes]

        # 5
        # Se eliminan las columnas correspondientes
        dataframe = dataframe.drop(columns=columnas_a_eliminar)
        
        return dataframe
    except Exception as e:
        print(e)

# Función para acomodar las columnas

def acomodar_columnas(dataframe):
    dataframe = dataframe[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'trip_distance', 'total_amount',
       'pulocationid', 'dolocationid', 'passenger_count',
       'payment_type']]
    return dataframe


# Funcion para renombrar las columnas
def renombrar_columnas(dataframe):
    
    diccionario_de_renombre = {'tpep_pickup_datetime':"fecha_hora_subida", 'tpep_dropoff_datetime':"fecha_hora_bajada", 'trip_distance':"distancia_recorrida", 'total_amount':"monto_total",
       'pulocationid':"id_zona_subida", 'dolocationid':"id_zona_bajada", 'passenger_count':"cantidad_pasajeros",
       'payment_type':"tipo_pago"}
    
    dataframe = dataframe.rename(columns=diccionario_de_renombre)
    return dataframe

# Función para normalizar el dataset


def normalizar_dataset(dataframe):
    import pandas as pd
    # Completamos la columna "cantidad_pasajeros" con el valor de 1 dónde haya faltantes
    dataframe["cantidad_pasajeros"] = dataframe["cantidad_pasajeros"].fillna(1)
    # Lo pasamos a entero
    dataframe["cantidad_pasajeros"] = dataframe["cantidad_pasajeros"].astype(int)

    # Dónde el monto total sea negativo, lo cambiamos por su opuesto positivo
    dataframe.loc[dataframe["monto_total"] < 0, "monto_total"] = dataframe.loc[dataframe["monto_total"] < 0, "monto_total"] * -1

    # Obtenemos la media del monto total teniendo en cuenta aquellos valores dónde no es 0
    media_monto_total = round(dataframe[dataframe["monto_total"] != 0.0]["monto_total"].mean(), 2)
    # Cambiamos los valores dónde el monto total sea 0 por la media
    dataframe.loc[dataframe["monto_total"] == 0.0, "monto_total"] = media_monto_total

    return dataframe




