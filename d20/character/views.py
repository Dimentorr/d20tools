from django.shortcuts import render, redirect
from .models import Character, CharactersList
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.decorators import login_required
from transliterate import translit

import os
from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    img = Image.open(image)
    # create a BytesIO object
    img_io = BytesIO()
    # save image to BytesIO object
    img.save(img_io, 'JPEG', quality=60)
    # create a django-friendly Files object
    file_name, old_extension = os.path.splitext(image.name)
    name_file = file_name + '.jpeg'
    new_image = File(img_io, name=name_file)
    return new_image


def rename(name):
    name = name.replace(' ', '')
    return translit(name, language_code='ru', reversed=True)


def save_media(request, object_model):
    if 'logo' in request.FILES:
        logo_file = compress(request.FILES['logo'])
        object_model.logo.save(rename(logo_file.name), logo_file)
    else:
        object_model.logo = 'characters/default.jpg'


@login_required(login_url='/account/login/')
def character_menu(request):
    all_characters = Character.objects.filter(owner=request.user).all()
    context = {'characters': all_characters, }

    return render(request, 'character/characters_menu.html', context)


@login_required(login_url='/account/login/')
def character_list(request, id):
    character = Character.objects.filter(owner=request.user).get(pk=id)
    context = {'character': character, }
    if character_list := CharactersList.objects.filter(character=character):
        context['character_list'] = character_list
    return render(request, 'character/character_list.html', context)


@login_required(login_url='/account/login/')
def new_character(request):
    errors = []
    context = {}
    if request.method == 'POST' and 'Create' in request.POST:
        print(request.POST)
        if not request.POST.get('character_name') or len(request.POST.get('character_name').replace(' ', '')) < 3:
            print(request.POST.get('character_name'))
            errors.append('Имя персонажа должно содержать хотя-бы 3 символа!')
        elif not request.user.is_authenticated:
            errors.append('Вы должны быть авторизованы!')
        else:
            character = Character()
            character.owner = request.user
            character.name = request.POST.get('character_name')

            save_media(request, character)

            character.save()
            return redirect('character_list', character.id)

    context['errors'] = errors
    return render(request, 'character/new_character.html', context)
