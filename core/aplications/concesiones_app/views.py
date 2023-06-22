from django.shortcuts import render,redirect
from aplications.data.concesiones_data import obtener_informacion
from .models import Concesiones
import json

from .models import Concesiones
# Create your views here.


def cargar_datos(request):

    # Llamar a la función para obtener la información y generar el archivo JSON

    json_data = obtener_informacion()
    
    for data in json_data:
        json_string = json.dumps(data)
        json_dict  = json.loads(json_string)
        print(data)
        concesiones = Concesiones(
            numero_concesion = json_dict['numero_concesion'],
            numero = int(json_dict['numero']),
            tipo_concesion = json_dict['tipo_concesion'],
            comuna = json_dict['comuna'],
            lugar = json_dict['lugar'],
            rs_ds = json_dict['rs/ds'],
            tipo_tramite = json_dict['tipo_tramite'],
            concesionario = json_dict['concesionario'],
            tipo_vigencia = json_dict['tipo_vigencia']
        )
        
        concesiones.save()

    return redirect('listar-datos')

def listar_datos(request):
    queryset = Concesiones.objects.all().order_by('numero')

    context = {
        'data':queryset
    }

    return render(request,'concesiones/concesiones.html',context)