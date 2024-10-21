from django.shortcuts import render
from .models import Character, CharactersList


def character_menu(request):
    all_characters = Character.objects.filter(owner=request.user).all()
    context = {'characters': all_characters, }

    return render(request, 'character/characters_menu.html', context)


def character_list(request, id):
    character = Character.objects.filter(owner=request.user).get(pk=id)
    context = {'character': character, }
    if character_list := CharactersList.objects.filter(character=character):
        context['character_list'] = character_list
    return render(request, 'character/character_list.html', context)


def new_character(request):
    return render(request, 'character/new_character.html')