# Importación de librerías
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from google.cloud import storage
import os
import re
import requests

# URL del sitio web
url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'

# Configura el controlador de Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abre la página web
driver.get(url)

# Espera unos segundos para que el contenido se cargue
time.sleep(5)

# Encuentra todos los enlaces con extensión parquet y taxis amarillos
elements = driver.find_elements(By.XPATH, "//a[contains(@href, 'yellow_tripdata_') and contains(@href, '.parquet')]")

# Lista vacía para almacenar los enlaces
links = []

# Filtra los enlaces para los años 2022 a 2024
for element in elements:
    href = element.get_attribute('href')
    if re.search(r'202[2-4]', href):
        print(f"Enlace encontrado: {href}")
        links.append(href)

print(f"Total de enlaces encontrados: {len(links)}")

# Crear un DataFrame con los enlaces
df = pd.DataFrame(links, columns=['links'])

# Guarda los enlaces en un archivo CSV
df.to_csv('enlaces.csv', index=False)

# Cierra el controlador
driver.quit()

# Configuración de la autenticación de GCP

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'datalogic-taxis-ny-4d9c91e757e1.json'

# Creación de un cliente de GCP

client = storage.Client()
bucket_name = 'prueba_datalogic'
bucket = client.bucket(bucket_name)

for url in df['links']:
    file_name = url.split('/')[-1]
    response = requests.get(url)
    
    if response.status_code == 200:

        # Guardamos el archivo localmente
        with open(file_name, 'wb') as f:
            f.write(response.content)

        # Leemos el archivo con pandas y seleccionamos las columnas que nos interesan
        df_file = pd.read_parquet(file_name)
        df_file = df_file[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'passenger_count', 'trip_distance', 'PULocationID', 'DOLocationID', 'payment_type', 'total_amount']]

        # Separamos fecha y hora de subida y bajada
        df_file["fecha_subida_al_taxi"] = df_file["tpep_pickup_datetime"].dt.date
        df_file["fecha_bajada_al_taxi"] = df_file["tpep_dropoff_datetime"].dt.date

        df_file["hora_subida_al_taxi"] = df_file["tpep_pickup_datetime"].dt.time
        df_file["hora_bajada_al_taxi"] = df_file["tpep_dropoff_datetime"].dt.time

        # Dropeamos las columnas que traen fecha y hora
        df_file.drop(columns=['tpep_pickup_datetime', 'tpep_dropoff_datetime'], inplace=True)

        # Descartamos outliers (no vale la pena imputar por el bajo porcentaje)
        df_file = df_file[df_file["fecha_subida_al_taxi"] >= pd.Timestamp('2022-01-01').date()]

        # Guardamos el archivo preprocesado
        df_file.to_parquet(file_name, index=False)
        
        # Lo subimos a Cloud Storage
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_name)

        # Eliminamos el archivo local
        os.remove(file_name)

        print(f'Archivo {file_name} subido a Cloud Storage')

    else:
        print(f'Error en la descarga del archivo {file_name}')
        