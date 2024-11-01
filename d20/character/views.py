from django.db import transaction

from django.shortcuts import render, redirect
from .models import Character, CharactersList
from .models import save_character_classes, get_character_classes, clear_character_classes, create_classes_for_save
from rules.models import Classes, Race
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.decorators import login_required
from transliterate import translit

import os
from io import BytesIO
from PIL import Image
from django.core.files import File


stats = [
    ['strength', 'Сила', ['Атлетика']],
    ['dexterity', 'Ловкость', ['Акробатика', 'Ловкость рук', 'Скрытность']],
    ['constitution', 'Телосложение', []],
    ['intelligence', 'Интелект', ['Анализ', 'История', 'Магия', 'Природа', 'Религия']],
    ['wisdom', 'Мудрость', ['Восприятие', 'Выживание', 'Медицина', 'Проницательность', 'Уход за животными']],
    ['charisma', 'Харизма', ['Выступление', 'Запугивание', 'Обман', 'Убеждение']]
]


def compress(image):
    img = Image.open(image)
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


@transaction.atomic
def edit_character(request, character_list, character):
    """
    Вносит изменения в таблицы Character, CharactersList.
    Args:
        request : данные после отправки со страницы form с method=POST
        character_list (CharactersList): Объект листа персонажа.
        character (Character): Объект персонажа.
    Returns:
        errors: Список ошибок, при сохранении данных.
    """
    errors = []
    print('Save')
    print(request.POST)
    try:
        # Если файл будет выбран, тогда 'logo' необходимо искать уже в FILES
        if 'logo' not in request.POST: save_media(request, character)
        if name := request.POST.get('name'): character.name = name
        if int(request.POST.get('lvl')) > 0: character_list.lvl = int(request.POST.get('lvl'))
        if int(request.POST.get('exp')) > 0: character_list.exp = int(request.POST.get('exp'))
        if classes := request.POST.getlist('class'):
            character_classes = [Classes.objects.get(pk=int(i)) for i in classes if i != '']
            save_character_classes(character, character_classes, request.POST.getlist('lvl_class'))
        character.save()
        character_list.save()
    except Exception as e:
        print(e)
        return e

    return errors


@login_required(login_url='/account/login/')
def character_list(request, id):
    character = Character.objects.filter(owner=request.user).get(pk=id)
    list_character = CharactersList.objects.get(character=character)
    races = Race.objects.all()
    classes = Classes.objects.all()

    if request.method == 'POST':
        if 'Back' in request.POST:
            return redirect('character_menu')
        elif 'Save' in request.POST:
            edit_character(request,
                           character_list=CharactersList.objects.get(character=character),
                           character=character)
            return redirect('character_list', character.pk)

    character_classes = get_character_classes(character)
    context = {'character': character,
               'stats': stats,
               # 'skills': skills,
               'list_character': list_character,
               'races': races,
               'classes': classes,
               'character_classes': character_classes,}
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
            CharactersList(character=character).save()
            return redirect('character_list', character.id)

    context['errors'] = errors
    return render(request, 'character/new_character.html', context)
