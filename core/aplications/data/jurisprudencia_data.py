from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def cargar_data():
    url = "https://www.buscadorambiental.cl/buscador/#/jurisprudencia"
    payload = {
        "search": "caratulado"
        # Agrega los demás parámetros necesarios para la solicitud POST
    }

    # Configura el driver de Selenium (en este ejemplo, se utiliza Chrome)
    driver = webdriver.Chrome()
    driver.get(url)

    # Espera a que la página se cargue completamente (puedes ajustar el tiempo según sea necesario)
    wait = WebDriverWait(driver, 10)
    try:
        #results_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".resultado")))

        # Encuentra el campo de búsqueda y envía los parámetros
        search_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        search_input.send_keys(payload["search"])

        # Encuentra el botón de búsqueda y haz clic en él
        search_button = driver.find_element(By.CSS_SELECTOR, "img.ng-star-inserted")
        search_button.click()

        # Espera a que se carguen los resultados de la solicitud POST
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".contenido")))

        # Procesa y muestra los resultados obtenidos

        # clean_resultados = []
        # for result in results:
        #     lines = result.text.splitlines()
        #     clean_lines = [line.strip() for line in lines]
        #     filtered_lines = list(filter(None, clean_lines))
        #     clean_resultados = [item.split(":")[-1].strip() for item in filtered_lines]
        return results
    finally:
        # Cierra el driver de Selenium después de completar la extracción
        driver.quit()


