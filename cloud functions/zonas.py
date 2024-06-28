import pandas as pd
import pyarrow
import numpy as np
from google.cloud import bigquery


def trigger_zonas(event, context):

  bucket = event["bucket"]
  name = event["name"]
  df = pd.read_csv(f'gs://{bucket}/{name}')

  # Filtramos sólo las zonas que pertenecen a Manhattan
  df = filtrar_manhattan(df)

  # Renombramos las columnas
  df = renombrar_columnas(df)

  # Cargamos el df a BigQuery
  cargar_a_bigquery(df)

def filtrar_manhattan(df):

  print(f'Shape del dataset antes del filtrado: {df.shape}')

  # Filtrar las zonas de Manhattan
  df = df[df['Borough'] == 'Manhattan']

  print(f'Shape del dataset despues del filtrado: {df.shape}')

  # Borramos la columna Borough ya que es redundante
  df = df.drop(columns='Borough')

  print(f'Shape del dataset despues de borrar borough: {df.shape}')
    
  return df

def renombrar_columnas(df):

  df.rename(columns={
      'LocationID': 'id_zona',
      'Zone': 'zona',
      'service_zone': 'zona_servicio'
      }, inplace=True)

  print(f'Shape del dataset despues de renombrar: {df.shape}')
  
  return df

def cargar_a_bigquery(df):

  client = bigquery.Client()
  table_id = "datalogic-taxis-ny.taxis.viajes_zonas"

  job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )
    
  job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
  job.result() 

  print(f"{job.output_rows} filas cargadas en {table_id}.")