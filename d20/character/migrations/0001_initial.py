# Generated by Django 5.1.2 on 2024-10-21 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='characters/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Персонаж',
                'verbose_name_plural': 'Персонажи',
            },
        ),
        migrations.CreateModel(
            name='CharactersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.CharField(max_length=50)),
                ('exp', models.IntegerField(default=0)),
                ('lvl', models.IntegerField(default=0)),
                ('class_defense', models.IntegerField(default=0)),
                ('initiative', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('max_hits', models.IntegerField(default=0)),
                ('now_hits', models.IntegerField(default=0)),
                ('temp_hits', models.IntegerField(default=0)),
                ('inspiration', models.BooleanField(default=0)),
                ('strength', models.IntegerField(default=10)),
                ('dexterity', models.IntegerField(default=10)),
                ('constitution', models.IntegerField(default=10)),
                ('intelligence', models.IntegerField(default=10)),
                ('wisdom', models.IntegerField(default=10)),
                ('charisma', models.IntegerField(default=10)),
                ('strength_saving', models.BooleanField(default=0)),
                ('dexterity_saving', models.BooleanField(default=0)),
                ('constitution_saving', models.BooleanField(default=0)),
                ('intelligence_saving', models.BooleanField(default=0)),
                ('wisdom_saving', models.BooleanField(default=0)),
                ('charisma_saving', models.BooleanField(default=0)),
                ('death_failed', models.IntegerField(default=0)),
                ('death_succeeded', models.IntegerField(default=0)),
                ('copper', models.IntegerField(default=0)),
                ('silver', models.IntegerField(default=0)),
                ('gold', models.IntegerField(default=0)),
                ('platinum', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.character')),
                ('class_character', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='rules.classes')),
                ('race', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='rules.race')),
            ],
            options={
                'verbose_name': 'Лист',
                'verbose_name_plural': 'Листы',
            },
        ),
    ]