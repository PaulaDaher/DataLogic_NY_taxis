# EDA

**Existen varios criterios para determinar la calidad de los datos de las fuentes identificadas, a continuación, menciono algunos de ellos:**

1. **Exactitud:** ¿Los datos son correctos y están libres de errores?
2. **Completitud:** ¿Están todos los datos necesarios presentes?
3. **Consistencia:** ¿Los datos son coherentes dentro del conjunto de datos y entre diferentes conjuntos de datos?
4. **Actualidad:** ¿Los datos están actualizados y son relevantes temporalmente?
5. **Relevancia:** ¿Los datos son pertinentes para el propósito específico del análisis?
6. **Accesibilidad:** ¿Los datos son fáciles de obtener y utilizar?
		
</br></br>

1. **Exactitud:** En los 3 conjuntos de datos principales que vamos a utilizar, recopilamos los datos de sus fuentes originales, ambos 3 están provistos por el gobierno de Nueva York, por lo cuál, **son exactos** en ese sentido. 

2. **Completitud:** El criterio de **Completitud** va a ser evaluado posteriormente en el proceso de EDA correspondiente a cada uno de los dataset.

3. **Consistencia:** Lo mismo sucede con el criterio de **Consistencia**, se aplicarán las transformaciones necesarias en el proceso de ETL de cada dataset. Aunque inicialmente podríamos decir que si tienen ocnsistenciam, las modificaciones iniciales que les hicimos a los datasets fueron para dejar únicamente las columnas útiles / importantes / relevantes, dentro de las cuáles también incluimos aquellas que pueden relacionarse de alguna u otra manera con las otras columnas de los otros datasets mediante un modelo de entidad - relación que hicimos una vez tuvimos los datasets con las columnas que íbamos a usar.

4. **Actualidad:** En cuanto al criterio de **actualidad**, del conjunto de datasets que consideramos principales, decidimos tomar el periodo 2016-2019, que se dió hace 8-5 años atrás. La elección fue fundamentada en el hecho de que, en el dataset de los taxis, el periodo disponible era, 2009-2024, en el dataset del sonido el periodo disponible era 2016-2019 y en el dataset del aire 2005-2022. El periodo que mejor se ajustaba a los 3 conjuntos de datos era el del sonido, así que decidimos trabajar con esa porción de los datos. También elegimos utilizar los años 2016 a 2019 ya que 3 años es una muestra significativa para una buena investigación y conclusión de lo acontecido.

5. **Relevancia:** Con respecto a la **relevancia**, elegimos solo los datos de la ciudad más importante de NY porque es un reflejo de lo que sucede en el resto de las ciudades.

6. **Accesibilidad:** Por último, si, los datos son fáciles de obtener y de utilizar. Casi todos los datasets, con excepción del de taxis, son estáticos, por lo cuál, para obtenerlos, es cuestión de descargarlos de su fuente original.
En el caso de los taxis, tenemos bastantes datasets, uno por cada mes de los años 2016-2019, por lo cuál, utilizaremos un procedimiento de Web Scraping para extraer los datos de su fuente original.
