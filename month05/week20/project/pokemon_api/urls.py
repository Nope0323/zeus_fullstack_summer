from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon_page, name='pokemon_page'),
    path('api/', views.pokemon_api, name='pokemon_api'),
]
