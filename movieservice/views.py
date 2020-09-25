from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json
from django.http import JsonResponse
import urllib.request as req

#serialzers and models
from .serializers import MovieSerializer
from .models import Movies
from django.contrib.auth.models import User

# Create your views here.

api_key = '31983801561a84bd8ebd7fe2ac3e4685'
base_url = "https://api.themoviedb.org/3/discover/movie/?api_key="+api_key


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def helloworld(request):
    return JsonResponse({'message':'user is logged in successfully, Hello world !'}, status = status.HTTP_200_OK)
    #return Response ("this is a response")


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
@permission_classes([IsAuthenticated])
def add_movies(request):
    """
    This function adds movies from tmdb's database to our own database
    As in adding a movie to a user's list
    """
    query_id = request.data['id']
    id_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(query_id, api_key)
    
    connection = req.urlopen(id_url)
    data = json.loads(connection.read())
    #user
    current_user = request.user    

    #dict ! 
    movie = {
        "movie_id": query_id,
        "title": data['original_title'],
        "overview":data['overview'],
        "average_vote":data['vote_average'],
        #"user_rating":request.data['my rating']
        "user_id":current_user.id
    }
    # serializer
    serializer = MovieSerializer(data = movie)
    if serializer.is_valid():
        serializer.save()
    else:
        return JsonResponse({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    return JsonResponse({'The movie has been added successfully!': movie}, status= status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_movies(request):
    """
    Lists all the movies in the user's 
    """
    current_user = request.user
    movies = Movies.objects.filter(user_id=current_user.id)
    MovieData = MovieSerializer(movies, many=True).data
    movies = []
    for movie in MovieData:
        movies.append(movie)
    return JsonResponse({"data": movies}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user_rating(request):
    query = Movies.objects.filter(movie_id=request.data['movie_id'])
    current_user = request.user
    query.user_rating = request.data["user_rating"]
    query.user_id = current_user.id
    query.update()
    
    serializer = MovieSerializer(query)
    return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)  


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_movie(request):
    query = Movies.objects.filter(movie_id = request.data['id'])
    query.delete()
    serializer = MovieSerializer(query)
    return JsonResponse({'message':'movie has been deleted'}, status = status.HTTP_200_OK)



