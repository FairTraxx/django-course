from django.urls import path
from .views import helloworld, list_movies, search_movies, add_movies, list_user_movies, delete_movie

urlpatterns = [
    path('test/', helloworld),
    path('list/', list_movies),
    path('search/', search_movies),
    path('add/', add_movies),
    path('list_user/', list_user_movies),
    path('delete/', delete_movie)
    
]