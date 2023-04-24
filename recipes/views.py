from django.shortcuts import render

def home(request):
    return render(request,'recipes/home.html', context= {
        'nome': 'Carlos Magno'
    })