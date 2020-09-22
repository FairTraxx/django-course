from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json
from django.http import JsonResponse
import urllib.request as req

#serialzers 
from .serializers import MovieSerializer

# Create your views here.

api_key = '31983801561a84bd8ebd7fe2ac3e4685'
base_url = "https://api.themoviedb.org/3/discover/movie/?api_key="+api_key

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def helloworld(request):
    return JsonResponse({'message':'user is logged in successfully, Hello world !'}, status = status.HTTP_200_OK)


@api_view(['GET'])
def list_movies(request):
    """
    List movies from TMDB's database
    """
    connect = req.urlopen(base_url)
    data = json.loads(connect.read())
    movie_list = data['results']

    return JsonResponse({'the available movies are': movie_list }, status = status.HTTP_200_OK)


@api_view(['GET'])
def search_movies(request):
    """
    searches for movies in tmdb's database
    """
    movie_title = request.data['title']
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key, movie_title)
    connect = req.urlopen(search_movie_url)
    data = json.loads(connect.read())
    return JsonResponse({'search results': data['results']}, status= status.HTTP_200_OK)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def add_movies(request):
    """
    This function adds movies from tmdb's database to our own database
    As in adding a movie to a user's list
    """

    

