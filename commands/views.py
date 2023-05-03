from django.shortcuts import render

def home(request):
    return render(request,'commands/pages/home.html', context= {
        'nome': 'Carlos Magno'
    })