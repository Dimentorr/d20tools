from django.contrib import admin
from rules.models import Classes, Race
from personal_account.models import LogoAccount
from character.models import Character, CharactersList

# Register your models here.
admin.site.register(Classes)
admin.site.register(Race)
admin.site.register(LogoAccount)
admin.site.register(Character)
admin.site.register(CharactersList)