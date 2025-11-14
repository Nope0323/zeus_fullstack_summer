from django.utils import path
from . import views

urlpatterns = [
    path('pokemon/', views.pokemon_list, name='pokemon_list'),
]
