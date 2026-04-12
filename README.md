# Scraping Resultados de Admisión 2026 UNMSM 

## ¿Qué hace el proyecto?

El srcrip extrae los resultados de admisión de la Univeridad Nacional Mayor de San Marcos por medio de la bibliotéca Selenium en Python. Extrayendo información carrera por carrera y consolidando la información en un Data Frame en Excel


## ¿Cómo se instalan las dependencias?
pip install selenium
pip install webdriver-manager
pip install lxml
pip install unidecode
pip install pandas

## ¿Cómo correr el script?
python scraper.py

## ¿Qué contiene el output?
El output generado es un archivo denominado 'resultados_admisión.xlx' que contiene los resultados de admisión de todas las carreras de la UNMSM, incluyendo el código de postulante, nombres y apellidos, escuela (carrera a la que postuló), puntaje, mérito (en caso aplique) y las observaciones correspondientes


# API REST: RAWG Video Games Database

## ¿Qué hace esta sección?
En esta sección se hacen requests para analizar, extraer y comparar datos de diversos videojuegos en la plataforma RAWG por medio de un API Key. Se exploraron estadísticas generales, rankings, comparaciones y, finalmente, se exporta un top 20 de los mejores juegos a todo nivel.

## ¿Cómo obtener la API Key?
1. Crear una cuenta en https://rawg.io
2. Ir a https://rawg.io/apidocs
3. Hacer clic en "Get API Key"
4. Copiar la key y pegarla en el notebook como variable local

## ¿Cómo correr el notebook?
1. Abrir `api/tarea_rawg_api.ipynb` en Jupyter
2. Reemplazar `API_KEY` con tu key personal
3. Ejecutar todas las celdas en orden

## ¿Qué contiene el output?
Contiene los 20 mejores juegos de todos los tiempos según RAWG, con las columnas: nombre, rating, metacritic, fecha de lanzamiento y género principal.
