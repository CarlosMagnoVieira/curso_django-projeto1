from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/home.html', context= {
        'nome': 'Carlos Magno'
    })

def contato(request):
    return render(request, 'me-apague/temp.html')

def sobre(request):
    return HttpResponse('sobre')