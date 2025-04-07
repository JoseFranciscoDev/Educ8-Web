from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def materias(request):
    return render(request, 'core/pages/materias.html')


