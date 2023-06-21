from django.shortcuts import render,redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import *

# Create your views here.
def Obtener_datos(request):
    url = "https://www.buscadorambiental.cl/buscador/#/jurisprudencia"
 
    payload = {
        "search": f"{request.POST['search']}"
        # Agrega los demás parámetros necesarios para la solicitud POST
    }

    # Configura el driver de Selenium (en este ejemplo, se utiliza Chrome)
    driver = webdriver.Chrome()
    driver.get(url)

    # Espera a que la página se cargue completamente (puedes ajustar el tiempo según sea necesario)
    wait = WebDriverWait(driver, 10)
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

    for result in results:
        lines = result.text.splitlines()
        clean_lines = [line.strip() for line in lines]
        filtered_lines = list(filter(None, clean_lines))
        clean_resultados = [item.split(":")[-1].strip() for item in filtered_lines]
        resultado = Jurisprudencias(
                rol = clean_resultados[0],
                caratulado = clean_resultados[1],
                tribunal = clean_resultados[2],
                fecha_sentencia = clean_resultados[3],
                tipo_causa = clean_resultados[4],
                competencia = clean_resultados[5],
                materia = clean_resultados[6],
                ministro_redactor = clean_resultados[7],
            )
        resultado.save()
            
    # Cierra el driver de Selenium después de completar la extracción
    driver.quit()


    # Renderiza la respuesta o realiza cualquier otra acción necesaria
    return redirect('listar')

def Busqueda(request):
    
    return render(request, 'jurisprudencias/busqueda.html') 

def Listar(request):
    jurisprudencias = Jurisprudencias.objects.all()
    context = {"jurisprudencias":jurisprudencias}
    return render(request, 'jurisprudencias/listar.html',context) 