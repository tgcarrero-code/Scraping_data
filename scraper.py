from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import unidecode
import time
import re

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

url_unmsm="https://admision.unmsm.edu.pe/Website20262/A/A.html"
driver.get(url_unmsm)

url_carreras=driver.find_elements(By.CSS_SELECTOR, "table tbody tr td a")

links= []

for url in url_carreras:
    link=url.get_attribute("href")
    links.append(link)

df_final=[]

for carrera in links:
    time.sleep(10)
    driver.get(carrera)
    registros=driver.find_element(By.ID, "dt-length-0")
    for option in registros.find_elements(By.TAG_NAME, "option"):
        if option.text=="100":
            option.click()
            print(f"Cargando 100 registros para: {carrera}")
            time.sleep(10)

            try:
                tabla_resultados = driver.find_element(By.ID, "tablaPostulantes").get_attribute("outerHTML")
                tabla_final = pd.read_html(tabla_resultados)[0]
                df_final.append(tabla_final)
                print(f"Listo!")
            except Exception as e:
                print(f"Error en {carrera}: {e}")
