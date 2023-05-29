from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Luiz Otavio',
    })


def contato(request):
    return render(request, 'temp.html')


def sobre(request):
    return HttpResponse('SOBRE')
