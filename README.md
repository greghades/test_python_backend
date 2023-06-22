
# Prueba Tecnica

Acontinuación se hará entrega de lo realizado conforme a las siguientes especificaciones 

## Requerimiento 1
 https://www.buscadorambiental.cl/buscador/#/jurisprudencia
- Obtenga la petición POST (list) con las jurisprudencias.

- Crear una función que obtenga la información presentada en la petición.
- Crear un modelo para la información presentada en  la petición.

- Guardar en el modelo la información obtenida 
- Opcional.Generar vista en el administrador para visualizar la información obtenida.

- Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.


## Requerimiento 2
https://www.concesionesmaritimas.cl/

Librería requerida a utilizar: Selenium WebDriver
- Crear un script para obtener la información presentada en una tabla luego de filtrar.

- Los filtros a utilizar son los siguientes:
    - Región: II
    - Gobernación Marítima: Antofagasta
    - Capitanía de Puerto: Antofagasta
- El script deberá recorrer todas las páginas y obtener la información de las tablas.
- El script deberá crear un archivo .json con la información obtenida.
- Generar modelo para guardar la información obtenida.
- Opcional. Generar vista en el administrador para visualizar la información obtenida.
- Opcional. Generar una vista con la información en Bootstrap 5 u otro similar


## Installation

Clona el repositorio: git clone https://github.com/greghades/test_python_backend
```bash
  git clone https://github.com/greghades/test_python_backend
```

Crea un entorno virtual: 

```bash
  python -m venv env
```

Activa el entorno virtual:

```bash
  En Windows: env\Scripts\activate
  En macOS y Linux: source env/bin/activate
```
Instala las dependencias: 

```bash
  pip install -r req.txt
```
Ejecuta las migraciones: 
```bash
  python manage.py migrate
```

Inicia el servidor de desarrollo: python 
```bash
  python manage.py runserver
```
## Uso de aplicación
Accede a la aplicación en tu navegador web: http://127.0.0.1:8000/home/

**Entonces tendra 2 botones**

Imagen de pantalla:
https://prnt.sc/iAHNZF6FTov9

**El primer boton** dará a ejecutar el desafio 1
Una vez en la vista dada por http://127.0.0.1:8000/jurisprudencia/busqueda/

Puede introducir un texto de busqueda de Jurisprudencias
Recomendaciones de busqueda:
- Hombre
- Vida
- Muerte

Una vez hecho la busqueda la aplicación se encargará de buscar los resultados usando Selenium webdriver ya que como es una pagina web de carga dinamicas se debe utilizar esta herramienta ya que con requests no es posible realizar dicha acción 

Una vez realizada la busqueda se guardaran en un modelo y se mostraran los resultados por pantalla

Imagen de pantalla: https://prnt.sc/06tVFPlIOwf8

Tambien pueden ver los resultados desde el admin de django en la ruta: 
http://127.0.0.1:8000/admin/jurisprudencias_app/jurisprudencias/

**El segundo boton** realizará una busqueda al url proporcionada con la ruta 
http://127.0.0.1:8000/conseciones/datos-concesiones/

Esta realizara un extracción de los datos de todas las paginas generando un archivo llamado datos.json que a su vez es cargado en un modelo.

Una vez terminada la busqueda se mostraran los resultados por pantalla
Imagen:https://prnt.sc/WE6PIETyf5gs

vease tambien en el siguiente enlace
http://127.0.0.1:8000/admin/concesiones_app/concesiones/




## Conclusion
Espero que mi propuesta sea de su agrado y considerenlo como un MVP
Saludos y gracias por la oportunidad
