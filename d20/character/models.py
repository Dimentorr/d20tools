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


class CharactersList(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # main information
    class_character = models.ForeignKey(models_rules.Classes, on_delete=models.SET_DEFAULT, default='', blank=True)
    race = models.ForeignKey(models_rules.Race, on_delete=models.SET_DEFAULT, default='', blank=True)
    background = models.CharField(max_length=50, default='', blank=True)
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