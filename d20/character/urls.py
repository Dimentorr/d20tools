from django.urls import path
from . import views

urlpatterns = [
    path('character_menu/', views.character_menu, name='character_menu'),
    path('list/<int:id>', views.character_list, name='character_list'),
    path('new/', views.new_character, name='new_character'),
]
