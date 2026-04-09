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
