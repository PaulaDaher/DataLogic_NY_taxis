# <h1 align=left> DATA LOGIC / NYC Taxis & Carbon Emission </h1>

<p align="center">
<img src="images\datalogic banner.png" height=230>
</p>



# <h3 align=left>**`EQUIPO DE TRABAJO`**</h3>

- **Juan Carlos Garzón Rodríguez**  |  Científico de datos (Scrum manager)
- **José Santos Iparraguirre Mancino**  |  Ingeniero de Datos
- **Mateo Tagliaferro** |  Cientifico de Datos 
- **Paula Daher**  |  Analista de Datos 
- **Jesus Felipe Sepulveda Alvarez**  |  Analista de Datos

</br></br>

# ÍNDICE
- [Descripción del proyecto](#descripción-del-proyecto)
- [Objectivos](#objetivos)
- [Alcance del proyecto](#alcance-del-proyecto)
- [Arquitectura del proyecto](#arquitectura-del-proyecto)
- [Stack tecnológico](#stack-tecnológico)
- [Flujo de datos](#flujo-de-datos)
- [Riesgos del proyecto](#riesgos-del-proyecto)
- [Metodología de trabajo](#metodología-de-trabajo)
- [Diagrama gantt](#diagrama-gantt)
- [Key performance indicator](#key-performance-indicator)
- [Bibliografía complementaria](#bibliografía-complementaria)
- [Contacto](#contacto)  
  

</br></br>
      
# DESCRIPCIÓN DEL PROYECTO

🌳🤝📈 En **DataLogic** nos especializamos en proyectos de **ciencia de datos** para ayudar a las empresas a **transicionar hacia estrategias sostenibles y respetuosas con el medio ambiente**. Utilizando análisis avanzados y modelos predictivos, proporcionamos soluciones que optimizan la eficiencia operativa, reducen la huella de carbono y promueven la innovación ambiental. 

En respuesta a la creciente necesidad de sostenibilidad y eficiencia operativa en el transporte urbano de Nueva York, nuestra empresa consultora presenta una **propuesta analítica para la posible implementación de vehículos eléctricos (VE) en la flota de transporte de pasajeros**. Este proyecto estratégico se enfoca en la reducción de emisiones contaminantes y niveles de ruido y mejora de la competitividad en un mercado que valora la innovación y la responsabilidad ambiental.   
   
</br></br>

# OBJETIVOS

Como consultora, nuestra misión es ayudar a las empresas para que tomen decisiones informadas y responsables que beneficien tanto a sus operaciones como al planeta, es por ello que nuestro objetivo es proporcionar a la empresa de transporte de pasajeros **una base sólida para tomar decisiones sobre la posible inversión en una flota de vehículos eléctricos**, mediante el **análisis de datos históricos de los taxis de la ciudad de Nueva York**, y su impacto en la **calidad del aire** y la **contaminación sonora**.

Nos enfocaremos en realizar un análisis exhaustivo de datos y desarrollar modelos predictivos avanzados para evaluar el impacto ambiental en la implementación parcial o total de la flota de taxis eléctricos o híbridos. Nuestro objetivo es proporcionar recomendaciones estratégicas basadas en insights precisos, optimizando la eficiencia operativa y reduciendo la huella ambiental.

</br></br>

# ALCANCE DEL PROYECTO

- 🚕 **Enfoque en Taxis Amarillo**: Ante la existencia de distintos tipos de taxis en la ciudad de Nueva York, limitaremos nuestro análisis en el registros de recorridos de taxis amarillos debido a su representatividad en el tráfico de la ciudad y la abundancia de datos disponibles.

- 🌍 **Alcance geográfico**
Limitaremos el análisis al distrito de Manhattan. Aprovecharemos la disponibilidad de datos detallados en esta área geográfica. Es un distrito densamente poblado y transitado. También enfrenta problemas significativos de contaminación del aire y sonora. Su tamaño manejable permite un análisis detallado sin sobrecargar recursos, y la implementación de una flota de taxis aquí puede ser más coste-efectiva, con beneficios importantes debido a la alta densidad de población y usuarios de taxis.

- ⏰ **Alcance temporal**
Utilizaremos datos del 2016 al 2019, ya que este periodo ofrece una muestra significativa, y nos vimos limitados a este periodo por los otros datasets. 
Nos centraremos en los taxis amarillos que circularon en el distrito de Manhattan durante ese periodo, debido a que no tienen limitaciones geograficas cómo si los tienen los taxis verdes. 

- ➕ **Alcances complementarios**
Realizaremos un análisis exhaustivo de la oferta automotriz actual, evaluando las características tecnológicas de los vehículos eléctricos e híbridos. Esto incluirá la autonomía, la contaminación ambiental y sonora que producen, así como otros factores cruciales como los costos de adquisición y mantenimiento. Además, examinaremos la infraestructura disponible en la ciudad, enfocándonos en la distribución de los centros de carga eléctrica y los tiempos de carga asociados.

- ❌ Es importante también delimitar claramente lo que está **fuera del alcance**. No nos encargamos del diseño ni la fabricación de vehículos eléctricos, ni de asesoría legal detallada sobre regulaciones específicas. Tampoco abordaremos cambios estructurales significativos en la infraestructura urbana ni la gestión operativa diaria de la flota de vehículos eléctricos, incluyendo asignación de conductores y mantenimiento rutinario. Además, no se realizará un análisis exhaustivo de impactos socioeconómicos amplios en la comunidad o la fuerza laboral como parte de este proyecto.

</br></br>

# ARQUITECTURA DEL PROYECTO

## FUENTES DE DATOS 

- **Taxis:** Nuestra principal fuente de datos viene dada por el TLC, que son las siglas de Comisión de taxi y limusinas de la ciudad de Nueva York. Es la agencia responsable de la concesión de licencias y la regulación de los taxis con medallón amarillo, los vehículos de alquiler, las furgonetas de cercanías y los vehículos de para tránsito de la ciudad de Nueva York. [Link](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)  
Método de obtención: Web Scraping.

- **contaminacion_sonora:** dataset con información sobre la contaminación sonora en la ciudad de NY. [Link](https://zenodo.org/records/3966543)  
Método de obtención: Descarga del archivo .csv (datos estáticos)

- **contaminacion_aire:** dataset con información sobre la calidad del aire en la ciudad de NY. [Link](https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r/about_data)  
Método de obtención: Descarga del archivo .csv (datos estáticos)

- **Datos complementarios:** diferentes datasets referentes a la autonomía, costo y eficiencia operativa de los diferentes tipos de combustible que utilizan los vehículos.  
Fuente: Recolección de diferentes sitios y almacenamiento en nuestro Drive.  
Método de obtención: Descarga de los archivos (datos estáticos)  

</br>


> *Si quieres saber más de la selección de datasets puedes visitar: [Motivo de elección de datasets](eleccion_datasets.md)*

</br>

## STACK TECNOLÓGICO

<img src="https://img.shields.io/badge/Python-black?style=flat&logo=python" height="25"> <img src="https://img.shields.io/badge/Pandas-black?style=flat&logo=pandas" height="25"> <img src="https://img.shields.io/badge/Numpy-black?style=flat&logo=Numpy" height="25"> <img src="https://img.shields.io/badge/ScikitLearn-black?style=flat&logo=Scikit-Learn" height="25"> <img src="https://img.shields.io/badge/FastAPI-black?style=flat&logo=fastapi" height="25"> <img src="https://img.shields.io/badge/BeautifulSoup-black?style=flat&logo=coffeescript" height="25"> <img src="https://img.shields.io/badge/Power%20BI-black?style=flat&logo=Power%20bi" height="25"><img src="https://img.shields.io/badge/Google%20cloud-black?style=flat&logo=Google%20cloud" height="25"> <img src="https://img.shields.io/badge/Big%20query-black?style=flat&logo=big%20query" height="25"> <img src="https://img.shields.io/badge/Cloud%20functions-black?style=flat&logo=cloud%20functions" height="25">


# <h3 align=left>**`PYTHON`**</h3>

- Lenguaje de programación altamente flexible y fácil de aprender, lo que lo hace ideal para la manipulación de datos, el análisis y el desarrollo de modelos de machine learning.Cuenta con una amplia gama de bibliotecas especializadas para diversas tareas, facilitando un desarrollo rápido y eficiente.

- Librerías a utilizar:
    - **Pandas:** Ofrece estructuras de datos y herramientas de manipulación de datos muy potentes y flexibles. Facilita el análisis y la preparación de los datos antes de su procesamiento posterior.
	- **BeautifulSoup:** Permite extraer datos de sitios web de manera eficiente y estructurada.
	- **FastAPI:** Facilita el desarrollo de APIs rápidas y seguras para exponer modelos y servicios de datos.
	- **Scikit-Learn:** Facilita el desarrollo, entrenamiento y evaluación de modelos de machine learning.Proporciona herramientas simples y eficientes para la minería de datos y el análisis de datos.

# <h3 align=left>**`GOOGLE CLOUD PLATAFORM (GCP)`**</h3>

- GCP ofrece soluciones escalables y de alto rendimiento que pueden manejar grandes volúmenes de datos y complejas consultas de análisis. Proporciona una integración fluida entre sus servicios, facilitando la construcción de pipelines de datos eficientes.

- Servicios a utilizar:
    - **Cloud Storage:** Actúa como nuestro Data Lake, donde se almacenan los datos en estado bruto antes de ser procesados. Permite almacenar grandes volúmenes de datos de manera eficiente y segura.
    - **BigQuery:** Utilizado para almacenar y analizar grandes volúmenes de datos, aprovechando su capacidad de procesamiento masivo y sus capacidades de consulta SQL. Proporciona consultas rápidas y eficientes sobre grandes conjuntos de datos.
    - **Cloud Functions:** Facilita la automatización de tareas de ETL, permitiendo la limpieza, transformación y carga de datos de manera eficiente. Permite ejecutar funciones en respuesta a eventos específicos o programados, asegurando un flujo de datos continuo y actualizado.

# <h3 align=left>**`POWER BI`**</h3>
-  Proporciona herramientas potentes para crear visualizaciones interactivas y paneles de control interactivos.
- Conecta directamente con BigQuery, permitiendo aprovechar las capacidades de análisis y procesamiento de datos en tiempo real.
-  Permite a los usuarios finales, como los empresarios y decision makers, explorar y analizar datos de manera intuitiva, facilitando la toma de decisiones informadas.

</br>

## FLUJO DE DATOS

⛏️ **Extracción de datos de las fuentes arriba descriptas:**  
En este proyecto, realizamos web scraping en el sitio web oficial de la Comisión de Taxis y Limusinas de la Ciudad de Nueva York para recopilar archivos Parquet con datos históricos de viajes de taxis amarillos correspondientes al periodo 2016-2019. Complementamos nuestro conjunto de datos con información histórica sobre las concentraciones de monóxido de carbono (CO) en Manhattan obtenida a través de la API de OpenWeather, como tambien en la API de zenodo.org que nos permitió enriquecer el análisis de los patrones de movilidad en relación con los factores ambientales.


🔍 **EDA:**   
En el Análisis Exploratorio de Datos, cargamos y verificamos los datos de viajes de taxis amarillos, niveles de monóxido de carbono (CO) y niveles en decibelios relacionado al sonido en Nueva York. Realizamos un resumen estadístico, identificamos valores nulos, y visualizamos las distribuciones de variables clave como la distancia del viaje,  la concentración de CO y niveles en decibelios. Analizamos patrones temporales anuales y correlaciones entre variables para evaluar relaciones como la posible influencia de los niveles de CO y niveles de decibeles en el uso de taxis. También identificamos anomalías en los datos para garantizar su calidad.

> **Si quieres saber más sobre el proceso EDA realizado, puedes dirigirte al siguiente link o bien analizar los notebooks respectivos: [EDA](eda.md)*

🧹 **Transformación y limpieza de datos**   
En el proceso de transformación y limpieza de datos para este proyecto, se realizaron acciones clave para preparar los conjuntos de datos de viajes de taxis amarillos,  niveles de monóxido de carbono (CO) y niveles en decibelios en Manhattan entre 2016 y 2019. Se corrigieron formatos de fecha, se manejaron valores nulos eliminando filas o imputando valores, y se identificaron y trataron valores atípicos que podrían afectar el análisis. Además, se crearon nuevas variables derivadas en se normalizaron datos numéricos para mantener la consistencia y prepararlos para análisis posteriores. La eliminación de columnas irrelevantes también se llevó a cabo para enfocarse en los datos más relevantes para  aseguran la calidad y coherencia de los datos.

📥 **Ingesta de Datos:**    
Los datos previamente tratados y los obtenidos por webscraping de viajes de taxis, datos de zonas y servicios, así como datos de contaminación del aire y sonora se almacenarán en Cloud Storage como archivos en estado bruto.

⚙️ **Procesamiento de Datos:**  
Se ejecutarán pipelines automatizados utilizando Cloud Functions para limpiar y transformar los datos en Cloud Storage. Este proceso incluirá la validación de datos, corrección de errores y formatos, así como la eliminación de datos redundantes o incompletos.

💾 **Almacenamiento y Análisis:**  
Los datos limpios y procesados se cargarán en BigQuery, donde estarán disponibles para el análisis y consultas complejas mediante SQL. BigQuery proporcionará la escalabilidad necesaria para manejar grandes volúmenes de datos y consultas de alto rendimiento.

📈 **Visualización y Reportes:**    
Power BI se conectará directamente a BigQuery para la creación de paneles interactivos y reportes visuales. Esto permitirá a los stakeholders explorar y analizar los datos de manera intuitiva, identificar tendencias, y tomar decisiones informadas basadas en los resultados del análisis.

</br>

<p align="left">
<img src="images\arquitectura.png" height=290>
</p>


</br></br>

# RIESGOS DEL PROYECTO

Los principales riesgos en el proyecto de implementación de vehículos eléctricos en la flota de transporte de pasajeros en Nueva York incluyen: 
- **Calidad de los datos**, ya que información incompleta o inexacta podría llevar a conclusiones erróneas. Para esto se implementarán procesos rigurosos de limpieza y validación de datos.
- **Interpretación de los datos**, es fundamental una correcta interpretación de los resultados para evitar decisiones erróneas.
- La **precisión de los modelos predictivos** también es crucial, dada la complejidad de las variables ambientales y operativas. Se utilizará validación para asegurar la robustez del modelado.
- La **escalabilidad y eficiencia computacional** representan desafíos adicionales, dado que el manejo ineficiente de grandes volúmenes de datos puede ralentizar el análisis y aumentar los costos.  
- Es importante señalar que **eventos atípicos**, como los ocurridos en el año 2020 debido a la pandemia, pueden alterar los análisis predictivos y los resultados esperados.
   
**Mitigar estos riesgos requiere enfoques rigurosos en la gestión de datos, validación continua de modelos, cumplimiento normativo e integración efectiva de nuevas tecnologías, garantizando así resultados confiables y relevantes.*
</br></br>

# METODOLOGÍA DE TRABAJO

# <h3 align=left>**`SCRUM`**</h3>
Desde la consultora abordaremos este proyecto en particular con la **metodología Scrum**. Scrum propone un **marco de trabajo ágil** a través del cual podemos abordar problemas complejos adaptativos a la vez que se entregan productos de forma eficiente y creativa con el máximo valor. Así, Scrum es una metodología que ayuda a los equipos a colaborar y realizar un trabajo de alto impacto. La metodología Scrum proporciona un** plan de valores, roles y pautas para ayudar al equipo a concentrarse en la iteración y la mejora continua en proyectos complejos**.

</br>

# DIAGRAMA GANTT

<p align="left">
<img src="images\gantt.png" height=400>
</p>


> **EC>** Equipo de trabajo completo  
> **ID>** Ingeniero de datos  
> **CD>** Científico de datos  
> **AD>** Analista de datos

</br></br>

# KEY PERFORMANCE INDICATOR

# <h3 align=left>**`☁️ KPI #1 Contaminación del aire`**</h3>
### Reducir la tasa de emisiones de CO2 promedio en un 5% con respecto al año anterior con la incorporación de 250 unidades de la flota a vehículos eléctricos

*La incorporación de 250 taxis eléctricos en la ciudad de Nueva York, en el distrito de Manhattan podría disminuir el promedio en un 5% las emisiones de CO2 con respecto al año anterior en base al periodo 2016 - 2019.*  

🧮 **Calculo**: Tasa de emisión = [(Promedio de emisiones de CO2 año anterior - Promedio de emisiones de CO2 año actual) / Promedio de emisiones de CO2 año anterior] * 100 


# <h3 align=left>**`🔊 KPI #2 Contaminación sonora`**</h3>
### Reducir en un 18% el ruido ambiental con respecto al año anterior con la incorporación de 250 unidades de la flota de vehículos eléctricos

*La incorporación de 250 taxis eléctricos en la ciudad de Nueva York, en el distrito de Manhattan podría disminuir en un 18% la contaminación sonora con respecto al año anterior en base al periodo 2016 - 2019.*

🧮 **Calculo**: Tasa de ruido = [(Contaminación sonora del año anterior - contaminación sonora del año actual) / Contaminación sonora del año anterior] * 100

	
# <h3 align=left>**`💸 KPI #3 Variabilidad de ingresos`**</h3>
### Incrementar los ingresos anualmente en un 5% con respecto al año anterior con la incorporación de 250 unidades de la flota de vehículos eléctricos

*La incorporación de 250 taxis eléctricos, podría aumentar en un 5% los ingresos por concepto de tarifas de servicio Taxi de la ciudad de Nueva York en el distrito de Manhattan en base al periodo 2016 - 2019.*


🧮 **Calculo**: Tasa de variación de ingresos = [(Ingresos totales año anterior - ingresos totales del año actual) / ingresos totales del año anterior] * 100



</br></br>


# BIBLIOGRAFÍA COMPLEMENTARIA

Conciencia corporativa ambiental:
- [Sustainable business](https://net0.com/blog/sustainable-business)
- [Why sustainability is crucial for corporate strategy?](https://www.weforum.org/agenda/2022/06/why-sustainability-is-crucial-for-corporate-strategy/)
- [Beneficios empresa medio ambiente](https://www.up-spain.com/blog/beneficios-empresa-medio-ambiente/)

</br></br>

# CONTACTO

📧 datalogic.grupo@gmail.com