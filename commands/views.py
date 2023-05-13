from django.shortcuts import render
from .models import Commands
from utils.commands.factory import make_command

def home(request):

    all_commands = Commands.objects.all().order_by('-id')
    print(all_commands[0].id)
    return render(request,'commands/pages/home.html', context= {
        'commands': all_commands
    })

def command(request, id):
    comando= Commands.objects.get(id=id)
    return render(request,'commands/pages/command-view.html', context= {
        'comando': comando,
        'is_detail_page': True,
    })

def language(request, language_id):
    commands_linguagem = Commands.objects.filter(
        language__id=language_id
        ).order_by('-id')
    return render(request,'commands/pages/home.html', context= {
        'commands': commands_linguagem,        
    })

