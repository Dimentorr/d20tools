from django.db import models
from django.contrib.auth.models import User
from rules import models as models_rules


class Character(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='characters/', default='characters/default.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class CharacterClass(models.Model):
    game_class = models.ForeignKey(models_rules.Classes, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.game_class.name} - {self.level}'


class CharactersList(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # main information
    class_character = models.ManyToManyField(CharacterClass)
    race = models.ForeignKey(models_rules.Race, on_delete=models.SET_DEFAULT, default='', null=True, blank=True)
    background = models.CharField(max_length=50, default='', null=True, blank=True)
    exp = models.IntegerField(default=0)
    lvl = models.IntegerField(default=1)
    # description
    #TODO
    # как сделать хранение списка предметов, у каждого из которого в идеале должны быть свойства
    # character_traits =
    # ideals =
    # attachments =
    # weaknesses =
    # battle stats =
    class_defense = models.IntegerField(default=10)
    initiative = models.IntegerField(default=0)
    speed = models.IntegerField(default=30)
    max_hits = models.IntegerField(default=0)
    now_hits = models.IntegerField(default=0)
    temp_hits = models.IntegerField(default=0)
    # вдохновение
    inspiration = models.BooleanField(default=0)
    # stats
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    # saving throws
    strength_saving = models.BooleanField(default=False)
    dexterity_saving = models.BooleanField(default=False)
    constitution_saving = models.BooleanField(default=False)
    intelligence_saving = models.BooleanField(default=False)
    wisdom_saving = models.BooleanField(default=False)
    charisma_saving = models.BooleanField(default=False)
    # saving throws death
    death_failed = models.IntegerField(default=0)
    death_succeeded = models.IntegerField(default=0)
    # bag
    copper = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    platinum = models.IntegerField(default=0)
    #TODO
    # как сделать хранение списка предметов, у каждого из которого в идеале должны быть свойства

    # skills
    #TODO
    # тот же вопрос

    # other skills
    #TODO
    # тот же вопрос

    def __str__(self):
        return f'List for character: {self.character}'

    class Meta:
        verbose_name = 'Лист'
        verbose_name_plural = 'Листы'


def create_classes_for_save(character, classes, lvl_classes):
    """
    Собирает классы персонажа в объекте таблицы CharactersList.
    Args:
        character (Character): Объект персонажа, которому нужно добавить классы.
        classes (list): Список классов (объекты Classes) для добавления.
    """
    character_list, created = CharactersList.objects.get_or_create(character=character)

    # Преобразование списка Classes в список CharacterClass
    character_classes = list()
    for i in range(len(classes)):
        if game_class := classes[i]:
            character_classes.append(CharacterClass.objects.create(game_class=game_class, level=lvl_classes[i]))

    character_list.class_character.set(character_classes)
    return character_list

def save_character_classes(character, classes, lvl_classes):
    """
    Сохраняет классы персонажа в таблицу CharactersList.
    Args:
        character (Character): Объект персонажа, которому нужно добавить классы.
        classes (list): Список классов (объекты Classes) для добавления.
    """
    create_classes_for_save(character, classes, lvl_classes).save()


def get_character_classes(character):
    """
    Получает классы персонажа из таблицы CharactersList.
    Args:
        character (Character): Объект персонажа, у которого нужно получить классы.
    Returns:
        list: Список классов (объекты CharacterClass) персонажа.
    """
    character_list = CharactersList.objects.get(character=character)
    return character_list.class_character.all()


def clear_character_classes(character_list):
    return character_list.class_character.all().delete()
