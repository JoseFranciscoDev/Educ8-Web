from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, 'core/index.html')

def materias(request):
    materias = Materia.objects.all()
    return render(request, 'core/pages/materias.html', {'materias': materias})
