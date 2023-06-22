import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# Ruta al archivo chromedriver.exe (asegúrate de tener la versión adecuada para tu Chrome)
CHROME_DRIVER_PATH = 'ruta/al/chromedriver.exe'

def obtener_informacion():
    # Configurar Selenium
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.concesionesmaritimas.cl')
    
    driver.switch_to.frame('centro_sigmar')

    iframe_element = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe_element)

    try:
        # Esperar a que la página cargue completamente
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//table')))

        # Realizar la búsqueda con los campos de selección 

        #Campo de Región
        select_element = Select(driver.find_element(By.XPATH, '//select[@name="variableRegion"]'))
        select_element.select_by_visible_text('II')

        #Campo de Gobierno
        select_element = Select(driver.find_element(By.XPATH, '//select[@name="variableGobmar"]'))
        select_element.select_by_visible_text('GOBERNACIÓN MARÍTIMA ANTOFAGASTA')

        #Campo de Puerto
        select_element = Select(driver.find_element(By.XPATH, '//select[@name="variableCapuerto"]'))
        select_element.select_by_visible_text('ANTOFAGASTA')

        # Hacer clic en el botón de búsqueda
        driver.find_element(By.XPATH, '//img[@name="verlistado"]').click()

        # Esperar a que los resultados de la búsqueda se carguen
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//table')))

       
        # Lista para almacenar los datos obtenidos
        datos = []

        pagina_actual = 1
        paginas = driver.find_element(By.XPATH,'//font[@color="#354A84"]/table')
        total_paginas = len(paginas.find_elements(By.XPATH,'.//td/font')) 

        while pagina_actual <= total_paginas:

            # Obtener la información de las tablas
            tabla_element = driver.find_element(By.XPATH, '//table[@style="font-family: Arial; font-size: 10 px; color: #000080; border: 2 ridge #F8CE62"]')
            filas = tabla_element.find_elements(By.XPATH, './/tr')
            filas = filas[1:]


            for fila in filas:
                celdas = fila.find_elements(By.TAG_NAME, 'td')
                if len(celdas) > 0:
                    # Obtener los valores de las celdas y almacenarlos en un diccionario
                    informacion = {
                        'numero': celdas[0].text,
                        'numero_concesion': celdas[1].text,
                        'tipo_concesion': celdas[2].text,
                        'comuna': celdas[3].text,
                        'lugar': celdas[4].text,
                        'rs/ds': celdas[5].text,
                        'tipo_tramite': celdas[6].text,
                        'concesionario': celdas[7].text,
                        'tipo_vigencia': celdas[8].text,

                        # Agrega más campos según la estructura de las tablas
                    }
                    datos.append(informacion)

             # Verificar si hay más páginas disponibles
            try:
                # Verificar si hay más páginas disponibles
                siguiente_element = driver.find_element(By.XPATH, f'//font/a[text()="{pagina_actual + 1}"]')
                siguiente_element.click()
                time.sleep(2)  # Esperar a que la siguiente página cargue completamente
                pagina_actual += 1
            except NoSuchElementException:
                break

        # Generar archivo JSON con los datos obtenidos
        with open('datos.json', 'w') as archivo_json:
            json.dump(datos, archivo_json, indent=4)

        with open('datos.json', 'r') as archivo:
            data = json.load(archivo)
            return data
    finally:
        # Cerrar el navegador
        driver.quit()



