from django.urls import path
from . import views
# from .views import pokemon_api, pokemon_list

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),
    # path("api/pokemon/", pokemon_api, name="pokemon_api"),
]
 