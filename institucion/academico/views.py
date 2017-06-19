# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.template import RequestContext

from academico.models import *
from academico.forms import *
import json


def index(request):
    """
    """
    diccionario = {'saludo': "Hola Mundo"}
    return render(request, 'index.html', diccionario, 
                  context_instance=RequestContext(request))


def listado_materias(request):
    """
        obtengo las materias 
    """
    materias = Materia.objects.all()
    diccionario = {'materias': materias, 'mensaje': 'Mensaje de la pantalla'}
    return render(request, 'listado_materias.html', diccionario, 
        context_instance=RequestContext(request))


def materia(request, id):
    """
        obtengo las materias 
    """
    materia = Materia.objects.get(pk=id)
    numero_paralelos = Paralelo.objects.filter(la_materia=materia).count()
    numero_estudiantes = Estudiante.objects.filter(
            paraleloestudiante__la_paralelo__la_materia=materia).count()
    diccionario = {'materia': materia, 'numero_paralelos': numero_paralelos,
                   'mensaje': 'Mensaje de la pantalla', 
                   'numero_estudiantes': numero_estudiantes}
    return render(request, 'materia.html', diccionario, 
                  context_instance=RequestContext(request))


def listado_paralelos(request):
    """
    """
    paralelos = Paralelo.objects.all()
    diccionario = {'paralelos': paralelos, 'mensaje': 'Listado de paralelos'}
    return render(request, 'listado_paralelos.html', diccionario, 
                  context_instance=RequestContext(request))


def paralelo_buscador(request, id):
    abecedario = [
            ('-', '-'),
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E'),
            ('F', 'F'),
            ('G', 'G'),
            ('H', 'H'),
            ('I', 'I'),
            ('J', 'J'),
            ('K', 'K'),
            ('M', 'M'),
            ('N', 'N'),
            ('O', 'O'),
            ('P', 'P'),
            ('Q', 'Q'),
            ('R', 'R'),
            ('S', 'S'),
            ('T', 'T'),
            ('W', 'W'),
            ('X', 'X'),
            ('Y', 'Y'),
            ('Z', 'Z'),
            ]
    paralelo = Paralelo.objects.get(pk=id)
    diccionario = {'abecedario': abecedario, 'paralelo': paralelo}
    
    return render(request, 'paralelo_buscador.html', diccionario)


@csrf_exempt
def funcion_ajax_buscador(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        letra = request.POST.getlist('valor')[0]
        id_paralelo = request.POST.getlist('id_paralelo')[0]
        estudiantes = Estudiante.objects.filter(paraleloestudiante__la_paralelo__id_paralelo=id_paralelo, apellido__startswith=letra).all()
        paralelo = Paralelo.objects.get(pk=id_paralelo)
        estudiantes = json.dumps([{'nombre': o.nombre, 'apellido': o.apellido} for o in estudiantes] )
        paralelo = json.dumps({'nombre': paralelo.nombre})
        req['mensaje'] = 'Correcto .... cargando datos '
        req['paralelo'] = paralelo 
        req['estudiantes'] = estudiantes 

        return JsonResponse(req, safe=False)


def paralelos_periodo(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ParaleloPeriodoForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL (opcional)
            id_periodo = request.POST['periodo']
            print id_periodo
            periodo = Periodo.objects.get(pk=id_periodo)
            paralelos = Paralelo.objects.filter(la_periodo=periodo)
    # if a GET (or any other method) we'll create a blank form
    else:
        paralelos = Paralelo.objects.all()
        form = ParaleloPeriodoForm()
        
    return render(request, 'paralelos_periodo.html', {'form': form, 'paralelos': paralelos})
