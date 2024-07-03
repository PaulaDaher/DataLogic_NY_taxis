# <h1 align='center'> DATA LOGIC / NYC Taxis & Carbon Emission </h1>

<p align="center">
<img src="images\datalogic banner.png" height=230>
</p>

# <h3 align=left>**EQUIPO DE TRABAJO** </h3>

- **Juan Carlos Garzón Rodríguez**  |  Científico de datos (Scrum manager)
- **José Santos Iparraguirre Mancino**  |  Ingeniero de Datos
- **Mateo Tagliaferro** |  Cientifico de Datos
- **Paula Daher**  |  Analista de Datos
- **Jesus Felipe Sepulveda Alvarez**  |  Analista de Datos

</br></br>

# ÍNDICE

- [Resumen](#resumen)
- [Descripción del proyecto](#descripción-del-proyecto)
- [Objectivos](#objetivos)
- [Alcance del proyecto](#alcance-del-proyecto)
- [Fuentes de datos](#fuentes-de-datos)
- [Stack tecnológico](#stack-tecnológico)
- [Flujo de datos](#flujo-de-datos)
- [Riesgos del proyecto](#riesgos-del-proyecto)
- [Metodología de trabajo](#metodología-de-trabajo)
- [Diagrama gantt](#diagrama-gantt)
- [Key performance indicator](#key-performance-indicator)
- [Bibliografía complementaria](#bibliografía-complementaria)
- [Contacto](#contacto)

</br></br>

# RESUMEN

Durante este proyecto, realizaremos un análisis de los datos acerca del movimiento de los taxis amarillos en la ciudad de Nueva York en el distrito de Manhattan en el periodo 2022 - 2024. A partir de los resultados de nuestro análisis, presentaremos un informe a una empresa de buses que busca invertir en una nueva flota eléctrica de vehículos. Le informaremos tanto en la zona, cómo en el horario en el cuál le será más rentable desplegar su flota de vehículos eléctricos, basándonos en los datos históricos, y además le ofreceremos posibles tendencias futuras del mercado basadas en predicciones dadas por modelos de Machine Learning.
Además, facilitaremos la toma de decisión de la empresa ofreciendo posibles opciones de vehículos eléctricos, teniendo en consideración los mejores de ellos, y los que además están posibilitados para operar cómo taxis en la ciudad de Nueva York.

</br></br>

# DESCRIPCIÓN DEL PROYECTO

🌳🤝📈 En **DataLogic** realizamos trabajos de **ciencia de datos** para ayudar a las empresas a **transicionar hacia estrategias sostenibles y respetuosas con el medio ambiente**. 
Utilizando análisis avanzados y modelos predictivos, proporcionamos soluciones que optimizan la eficiencia operativa, reducen la huella de carbono, promueven la innovación ambiental mediante el desarrollo de modelos de negocio que además de lo anteriormente mencionado, incrementan las ganancias de las empresas.

En respuesta a la creciente necesidad de sostenibilidad y eficiencia operativa en el transporte urbano de Nueva York, nuestra empresa consultora presenta una **propuesta analítica para algunas posibles implementaciones de vehículos eléctricos (VE) en la flota de transporte de pasajeros**. Este proyecto estratégico se enfoca en proporcionar la información adecuada para que la empresa que nos contactó tenga las estrategias y/o oportunidades para tomar las mejores decisiones, fundamentadas con datos. Cómo consecuencia de las mismas, en la ciudad habrá una reducción de emisiones contaminantes y en las calles los niveles de ruido disminuirán.
</br>

<p align="left">
<img src="images\portada taxi.png" height=180>
</p>

</br></br>

# OBJETIVOS

Nuestra misión es informar a las empresas para que tomen decisiones adecuadas y responsables que beneficien tanto a sus operaciones como al planeta, es por ello que le proporcionaremos a la empresa de transporte de pasajeros una **visión del comportamiento del mercado de los taxis en la ciudad de Nueva York en base a los datos históricos**. También le ofreceremos una **predicción del posible comportamiento futuro del mercado**. 
Para complementar nuestro análisis, decidimos sumar posibles vehículos eléctricos en los cuáles la empresa puede invertir para crear su nueva flota. Los mismos fueron elegidos prudentemente teniendo en especial consideración a aquellos vehículos que tienen permitido operar cómo taxis en la ciudad de Nueva York.
Con todo lo anteriormente mencionado, mediante una visualización clara de los datos, le **ofreceremos la solución más óptima posible en cuanto a la tasa inversión : beneficio**. Proporcionaremos recomendaciones estratégicas basadas en insights precisos, optimizando la eficiencia operativa y reduciendo la huella ambiental. 

</br></br>

# ALCANCE DEL PROYECTO

- 🚕 **Taxis amarillos**: Ante la existencia de distintos tipos de taxis en la ciudad de Nueva York, limitaremos nuestro análisis en el registros de recorridos de taxis amarillos debido a su representatividad en el tráfico de la ciudad y la abundancia de datos disponibles.

- 🌍 **Alcance geográfico**: Nuestro análisis será al distrito de Manhattan. Es un distrito densamente poblado y transitado, representando más de un 80% de los registros en la mayor parte de los meses. También enfrenta problemas significativos relacionados con la contaminación del aire y del sonido, por lo cuál, la implementación de las soluciones que ofrecemos, tendrán un impacto positivo en ese distrito. Su tamaño manejable y representativo permite un análisis detallado sin sobrecargar recursos, y la implementación de una flota de taxis aquí puede ser más rentable debido a lo anteriormente mencionado.

- ⏰ **Alcance temporal**: Utilizaremos datos del periodo 2022 - 2024, ya que este periodo ofrece una muestra significativa, actualizada, y post - pandemia.

- ➕ **Alcances complementarios**: Analizaremos la oferta automotriz actual, evaluando las características tecnológicas de los vehículos eléctricos, teniendo en especial consideración a aquellos modelos que actualmente se usan cómo taxis en la ciudad de Nueva York.
Nuestro análisis incluirá la autonomía, el precio, el modelo, el año de lanzamiento, los tiempos de carga de electricidad y también el costo de mantenimiento.
Tendremos en cuenta también las estaciones de servicio que disponen de carga eléctrica para que la implementación de los vehículos sea en el lugar más adecuado posible.

- ❌ **Fuera de nuestro alcance**: No nos encargamos del diseño ni de la fabricación de vehículos eléctricos, ni de asesoría legal detallada sobre regulaciones específicas. No abordaremos cambios estructurales en la infraestructura urbana, cómo tampoco la gestión operativa diaria de la flota de vehículos eléctricos, refiriendo con esto último a la asignación de conductores y mantenimiento rutinario. Además, no se realizará un análisis exhaustivo de impactos socioeconómicos amplios en la comunidad o la fuerza laboral como parte de este proyecto.
 
</br></br>

# FUENTES DE DATOS

### Principales

- **Viajes de los taxis:** Nuestra principal fuente de datos viene dada por el TLC, que son las siglas de Comisión de taxi y limusinas de la ciudad de Nueva York. Es la agencia responsable de la concesión de licencias y la regulación de los taxis con medallón amarillo, los vehículos de alquiler, las furgonetas de cercanías y los vehículos de para tránsito de la ciudad de Nueva York. [Link a la página](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)  

  Método de obtención: Web Scraping.

- **Autos eléctricos:** diferentes datasets referentes a la autonomía, costo y eficiencia operativa sobre autos eléctricos e híbridos.

  Fuente: Recolección de diferentes sitios y almacenamiento en nuestro Drive.

  Método de obtención: Descarga de los archivos (datos estáticos)

### Complementarios

- **Contaminación sonora:** dataset con información sobre la contaminación sonora en la ciudad de NY. [Link a la página](https://zenodo.org/records/3966543)

  Método de obtención: Descarga del archivo .csv (datos estáticos)

- **Contaminación del aire:** dataset con información sobre la calidad del aire en la ciudad de NY. [Link a la página](https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r/about_data)

  Método de obtención: Descarga del archivo .csv (datos estáticos)



</br>

> *Si quieres saber más de la selección de datasets puedes visitar: [Motivo de elección de datasets](eleccion_datasets.md)*

</br></br>

# ARQUITECTURA DEL PROYECTO

## STACK TECNOLÓGICO

<img src="https://img.shields.io/badge/Python-black?style=flat&logo=python" height="25"> <img src="https://img.shields.io/badge/Pandas-black?style=flat&logo=pandas" height="25"> <img src="https://img.shields.io/badge/Numpy-black?style=flat&logo=Numpy" height="25"> <img src="https://img.shields.io/badge/ScikitLearn-black?style=flat&logo=Scikit-Learn" height="25"> <img src="https://img.shields.io/badge/Power%20BI-black?style=flat&logo=Power%20bi" height="25"><img src="https://img.shields.io/badge/Google%20cloud-black?style=flat&logo=Google%20cloud" height="25"> <img src="https://img.shields.io/badge/Big%20query-black?style=flat&logo=big%20query" height="25"> <img src="https://img.shields.io/badge/Cloud%20functions-black?style=flat&logo=cloud%20functions" height="25">

# <h3 align=left>**PYTHON**</h3>

- Lenguaje de programación altamente flexible y fácil de aprender, lo que lo hace ideal para la manipulación de datos, el análisis y el desarrollo de modelos de machine learning. Cuenta con una amplia gama de bibliotecas especializadas para diversas tareas, facilitando un desarrollo rápido y eficiente.
- Principales librerías a utilizar:

  - **Pandas:** Ofrece estructuras de datos y herramientas de manipulación de datos muy potentes y flexibles. Facilita el análisis y la preparación de los datos antes de su procesamiento posterior.
  - **Selenium:** Permite extraer datos de sitios web de manera eficiente y estructurada.
  - **Streamlit:** Facilita el desarrollo de una interfaz web rápida y segura para exponer modelos y servicios de datos.
  - **Scikit-Learn:** Facilita el desarrollo, entrenamiento y evaluación de modelos de machine learning. Proporciona herramientas simples y eficientes para la minería de datos y el análisis de datos.

# <h3 align=left>**GOOGLE CLOUD PLATAFORM (GCP)**</h3>

- GCP ofrece soluciones escalables y de alto rendimiento que pueden manejar grandes volúmenes de datos y complejas consultas de análisis. Proporciona una integración fluida entre sus servicios, facilitando la construcción de pipelines de datos eficientes.
- Servicios a utilizar:

  - **Cloud Storage:** Actúa como nuestro Data Lake, donde se almacenan los datos en estado bruto antes de ser procesados. Permite almacenar grandes volúmenes de datos de manera eficiente y segura.
  - **BigQuery:** Utilizado para almacenar y analizar grandes volúmenes de datos, aprovechando su capacidad de procesamiento masivo y sus capacidades de consulta SQL. Proporciona consultas rápidas y eficientes sobre grandes conjuntos de datos.
  - **Cloud Functions:** Facilita la automatización de tareas de ETL, permitiendo la limpieza, transformación y carga de datos de manera eficiente. Permite ejecutar funciones en respuesta a eventos específicos o programados, asegurando un flujo de datos continuo y actualizado.

# <h3 align=left>**POWER BI**</h3>

- Proporciona herramientas potentes para crear visualizaciones interactivas y paneles de control interactivos.
- Conecta directamente con BigQuery, permitiendo aprovechar las capacidades de análisis y procesamiento de datos en tiempo real.
- Permite a los usuarios finales, como los empresarios y decision makers, explorar y analizar datos de manera intuitiva, facilitando la toma de decisiones informadas.

</br>

## FLUJO DE DATOS

⛏️ **Extracción de datos de las fuentes arriba descriptas:**
En este proyecto, realizamos web scraping en el sitio web oficial de la Comisión de Taxis y Limusinas de la Ciudad de Nueva York para recopilar archivos Parquet con datos históricos de viajes de taxis amarillos correspondientes al periodo 2022-2024. Complementamos nuestro conjunto de datos con información sobre autos eléctricos, su autonomía, eficiencia y costos operativos.

🔍 **EDA:** 
En el Análisis Exploratorio de Datos, cargamos y verificamos los datos para realizar un resumen estadístico, identificar valores nulos, y visualizar las distribuciones de variables clave. Analizamos patrones temporales anuales y correlaciones entre variables para evaluar relaciones como la posible influencia de los niveles de CO y niveles de decibeles en el uso de taxis. También identificamos anomalías en los datos para garantizar su calidad.

> **Si quieres saber más sobre el proceso EDA realizado, puedes dirigirte al siguiente link o bien analizar los notebooks respectivos: [EDA](eda/eda.md)*

🧹 **Transformación y limpieza de datos**
En el proceso de transformación y limpieza de datos para este proyecto, se realizaron acciones clave para preparar los conjuntos de datos. Se corrigieron formatos de fecha, se manejaron valores nulos eliminando filas o imputando valores, y se identificaron y trataron valores atípicos que podrían afectar el análisis. Además, se crearon nuevas variables derivadas en se normalizaron datos numéricos para mantener la consistencia y prepararlos para análisis posteriores. La eliminación de columnas irrelevantes también se llevó a cabo para enfocarse en los datos más relevantes para  aseguran la calidad y coherencia de los datos.

📥 **Ingesta de Datos:**
Los datos previamente tratados y los obtenidos por webscraping de viajes de taxis, datos de zonas y servicios, así como datos de contaminación del aire y sonora se almacenarán en Cloud Storage como archivos en estado bruto.

⚙️ **Procesamiento de Datos:**
Se ejecutarán pipelines automatizados utilizando Cloud Functions para limpiar y transformar los datos en Cloud Storage. Este proceso incluirá la validación de datos, corrección de errores y formatos, así como la eliminación de datos redundantes o incompletos.

💾 **Almacenamiento y Análisis:**
Los datos limpios y procesados se cargarán en BigQuery, donde estarán disponibles para el análisis y consultas complejas mediante SQL. BigQuery proporcionará la escalabilidad necesaria para manejar grandes volúmenes de datos y consultas de alto rendimiento.

📈 **Visualización y Reportes:**
Power BI se conectará directamente a BigQuery para la creación de paneles interactivos y reportes visuales. Esto permitirá a los stakeholders explorar y analizar los datos de manera intuitiva, identificar tendencias, y tomar decisiones informadas basadas en los resultados del análisis.

🤖 **Machine Learning:**
Desarrollamos modelos de Machine Learning para predecir la demanda futura para los viajes en taxis, un sistema de recomendación para invertir en diferentes autos eléctricos, y un chatbot para realizar preguntas sobre los mismos.

🎨 **Streamlit:**
Los productos finales fueron embebidos en nuestra app desarrollada con Streamlit, disponibilizando toda la información que necesita el cliente en el mismo sitio.

</br>

<p align="left">
<img src="images\arquitectura1.png" height=600>
</p>

</br></br>

# RIESGOS DEL PROYECTO

Los principales riesgos en el proyecto de implementación de vehículos eléctricos en la flota de transporte de pasajeros en Nueva York incluyen:

- **Calidad de los datos**, ya que información incompleta o inexacta podría llevar a conclusiones erróneas. Para esto se implementarán procesos rigurosos de limpieza y validación de datos.
- **Interpretación de los datos**, es fundamental una correcta interpretación de los resultados para evitar decisiones erróneas.
- La **precisión de los modelos predictivos** también es crucial, dada la complejidad de las variables ambientales y operativas. Se utilizará validación para asegurar la robustez del modelado.
- La **escalabilidad y eficiencia computacional** representan desafíos adicionales, dado que el manejo ineficiente de grandes volúmenes de datos puede ralentizar el análisis y aumentar los costos.
- Es importante señalar que **eventos atípicos**, como los ocurridos en el año 2020 debido a la pandemia, pueden alterar los análisis predictivos y los resultados esperados.

*Mitigar estos riesgos requiere enfoques rigurosos en la gestión de datos, validación continua de modelos, cumplimiento normativo e integración efectiva de nuevas tecnologías, garantizando así resultados confiables y relevantes.*
</br></br>

# METODOLOGÍA DE TRABAJO

# <h3 align=left>**SCRUM**</h3>

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

# <h3 align=left>**☁️ KPI #1 Cantidad de viajes**</h3>

### Aumentar la cantidad de viajes totales en un 15% con respecto al semestre anterior.

🧮 **Calculo**: Tasa de viajes = [(Suma de viajes totales semestre anterior anterior - Suma de viajes totales semestre actual) / Suma de viajes totales semestre anterior] * 100 

# <h3 align=left>**🔊 KPI #2 Flota de taxis**</h3>

### Sumar un vehículo a la flota de taxis eléctricos cada año.

*Se podría sumar un vehículo a la flota de taxis eléctricos cada 12 meses reinvirtiendo un 15% de la facturación en la incorporación de nuevos vehículos operativos*

🧮 **Calculo**: Dinero disponible para reinvertir = (Suma de facturación anual total de todos los taxis / Número de taxis de la flota) * 0.15

# <h3 align=left>**💸 KPI #3 Variabilidad de ingresos**</h3>

### Incrementar los ingresos anualmente en un 5% con respecto al año anterior.

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
