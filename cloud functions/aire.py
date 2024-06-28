import pandas as pd
import pyarrow
import numpy as np
from google.cloud import bigquery

def etl_aire(event, context):
    
    bucket = event["bucket"]
    name = event["name"]
    df = pd.read_csv(f'gs://{bucket}/{name}')
    
    diccionario_para_renombrar = {
        'Indicator ID': "id_indicador",
        'Name': "nombre_del_indicador",
        'Geo Type Name': "tipo_geografico",
        'Geo Join ID': "id_de_union_geografico",
        'Data Value': "valor_del_dato",
        'Geo Place Name': "nombre_del_barrio",
        'Measure Info': "unidad_de_medida",
        'Start_Date': "fecha_inicial",
        'Time Period': "periodo_de_tiempo"
    }
    
    df.rename(columns=diccionario_para_renombrar, inplace=True)
    
    df['año'] = df['periodo_de_tiempo'].apply(extract_year)
    df['descripcion_temporal'] = df['periodo_de_tiempo'].apply(extract_description)
    df['descripcion_temporal'] = df['descripcion_temporal'].fillna('')
    
    df['año'] = df['año'].astype(int)

    df = df[df['año'] >= 2018]

    # Seleccionar columnas relevantes después de renombrar
    columnas_relevantes = list(diccionario_para_renombrar.values()) + ['año', 'descripcion_temporal']
    df = df[columnas_relevantes]
    
    barrios_manhattan = [
        "Washington Heights", "Inwood", "Marble Hill", "Central Harlem", "East Harlem",
        "Upper East Side", "Yorkville", "Lenox Hill", "Roosevelt Island", "Upper West Side",
        "Lincoln Square", "Clinton", "Midtown", "Murray Hill", "Turtle Bay", "Gramercy",
        "Stuyvesant Town", "Chelsea", "Greenwich Village", "SoHo", "Lower East Side",
        "Tribeca", "Little Italy", "Chinatown", "Battery Park City", "Financial District"
    ]
    
    df = df[df['nombre_del_barrio'].isin(barrios_manhattan)]

    df.drop(columns='periodo_de_tiempo', inplace=True)
    
    cargar_a_bigquery(df)

def extract_year(text):
    import re
    match = re.search(r'\b\d{4}\b', text)
    return match.group(0) if match else None

def extract_description(text):
    import re
    match = re.search(r'\b\d{4}\b', text)
    if match:
        return text.replace(match.group(0), '').strip()
    else:
        return text

def cargar_a_bigquery(df):

    client = bigquery.Client()
    table_id = "datalogic-taxis-ny.taxis.contaminacion_aire"

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )
    
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Espera a que el trabajo de carga termine

    print(f"{job.output_rows} filas cargadas en {table_id}.")
