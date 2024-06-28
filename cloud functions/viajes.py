import pandas as pd
import pyarrow
import numpy as np
from google.cloud import bigquery


def trigger_viajes(event, context):

    # Obtenemos la ruta
    bucket = event["bucket"]
    name = event["name"]

    # Leemos el parquet
    df = pd.read_parquet(f'gs://{bucket}/{name}', engine='pyarrow')

    # Aplicamos las funciones
    renombrar_columnas(df)

    zonas_df = obtener_zonas_df()

    print(f'Shape del dataset antes del filtrado: {df.shape}')
    df = filtrar_manhattan(df, zonas_df)
    print(f'Shape del dataset despues del filtrado: {df.shape}')

    transformar_dataset(df)
    
    cargar_a_bigquery(df)

def renombrar_columnas(df):

    # Renombramos las columnas
    df.rename(columns={
        'passenger_count': 'cantidad_pasajeros',
        'trip_distance': 'distancia_recorrida',
        'PULocationID': 'zona_subida',
        'DOLocationID': 'zona_bajada',
        'payment_type': 'tipo_pago',
        'total_amount': 'monto_total'
    }, inplace=True)

def obtener_zonas_df():

    # Leemos el df de las zonas
    zonas_df = pd.read_csv('gs://taxis_viajes/taxi+_zone_lookup.csv')
    return zonas_df

def transformar_dataset(df):

    nulos_antes = df['cantidad_pasajeros'].isna().sum()
    print(f'Nulos en cantidad_pasajeros antes de imputar: {nulos_antes}')

    # Completamos la columna "cantidad_pasajeros" con el valor de 1 dónde haya faltantes
    df["cantidad_pasajeros"] = df["cantidad_pasajeros"].fillna(1)
    # Lo pasamos a entero
    df["cantidad_pasajeros"] = df["cantidad_pasajeros"].astype(int)

    nulos_despues = df['cantidad_pasajeros'].isna().sum()
    print(f'Nulos en cantidad_pasajeros despues de imputar: {nulos_despues}')

    # Dónde el monto total sea negativo, lo cambiamos por su opuesto positivo
    df.loc[df["monto_total"] < 0, "monto_total"] = df.loc[df["monto_total"] < 0, "monto_total"] * -1

    # Obtenemos la media del monto total teniendo en cuenta aquellos valores dónde no es 0
    media_monto_total = round(df[df["monto_total"] != 0.0]["monto_total"].mean(), 2)
    # Cambiamos los valores dónde el monto total sea 0 por la media
    df.loc[df["monto_total"] == 0.0, "monto_total"] = media_monto_total
    
    # Detección y eliminación de duplicados
    duplicados_antes = df.duplicated().sum()
    print(f'Duplicados antes de eliminar: {duplicados_antes}')
    df.drop_duplicates(inplace=True)
    duplicados_despues = df.duplicated().sum()
    print(f'Duplicados después de eliminar: {duplicados_despues}')

    return df

def filtrar_manhattan(df, zonas_df):

    # Filtrar las zonas de Manhattan
    manhattan_zonas = zonas_df[zonas_df['Borough'] == 'Manhattan']['LocationID']
    
    # Filtrar el DataFrame principal
    df = df[df['zona_subida'].isin(manhattan_zonas) | df['zona_bajada'].isin(manhattan_zonas)]
    
    return df

def cargar_a_bigquery(df):

    # Cliente de bigquery
    client = bigquery.Client()

    # Ruta de la tabla
    table_id = "datalogic-taxis-ny.taxis.viajes_taxis"


    # Configuracion del trabajo
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )
    
    # Carga a bigquery
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Espera a que el trabajo de carga termine

    print(f"{job.output_rows} filas cargadas en {table_id}.")