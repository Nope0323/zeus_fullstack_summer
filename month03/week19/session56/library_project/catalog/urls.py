from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/new/', views.create_book, name='book_create'),
    path('book/<int:pk>/edit/', views.update_book, name='book_update'),
    path('book/<int:pk>/delete/', views.delete_book, name='book_delete'),
]

