from django.urls import path
from .views import helloworld, list_movies, search_movies

urlpatterns = [
    path('test/', helloworld),
    path('list/', list_movies),
    path('search/', search_movies)
    
]