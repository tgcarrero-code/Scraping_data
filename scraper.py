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
