from django.shortcuts import render
from utils.commands.factory import make_command

def home(request):
    return render(request,'commands/pages/home.html', context= {
        'commands': [make_command() for _ in range(10)]
    })

def command(request, id):
    return render(request,'commands/pages/command-view.html', context= {
        'command': make_command(),
        'is_detail_page': True,
    })

