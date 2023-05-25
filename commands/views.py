from django.shortcuts import get_object_or_404, render
from utils.commands.factory import make_command

from .models import Commands


def home(request):

    all_commands = Commands.objects.filter(is_published=True).order_by('-id')
    return render(request, 'commands/pages/home.html', context={
        'commands': all_commands
    })


def command(request, id):
    comando = get_object_or_404(Commands, pk=id, is_published=True)
    return render(request, 'commands/pages/command-view.html', context={
        'comando': comando,
        'is_detail_page': True,
    })


def language(request, language_id):
    commands_linguagem = Commands.objects.filter(
        language__id=language_id,
        is_published=True
    ).order_by('-id')

    if commands_linguagem:
        return render(request, 'commands/pages/language.html', context={
            'commands': commands_linguagem,
            'language_name': 'Languague - ' + commands_linguagem.first().language.language_name,
        })
    else:
        return render(request, 'commands/pages/language.html', context={
            'language_name': 'Not found',
        })
