from django.shortcuts import render

from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.models import Director, Genre, Movie
from api.serializers import DirectorSerializer, GenreSerializer, MovieSerializer


class MovieView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'popularity', 'imdb_score', 'director__name', 'genre__name']

    # @permission_classes((IsAuthenticated, ))
    def post(self, request):
        if request.user.is_authenticated and request.user.username == 'admin':
            try:
                director_obj, _ = Director.objects.get_or_create(name=request.data.get('director'))
                # print(director_obj.name)
                each_movie_formatted = {
                    'name': request.data.get('name'),
                    'imdb_score': request.data.get('imdb_score'),
                    'popularity': request.data.get('99popularity'),
                    'director': director_obj
                }
                movie_obj, _ = Movie.objects.get_or_create(**each_movie_formatted)
                for each_genre in request.data.get('genre'):
                    genre_obj, _ = Genre.objects.get_or_create(name=each_genre)
                    movie_obj.genre.add(genre_obj)
                movie_obj.save()
                return Response("Data inserted successfully", status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(f"Bad Record:{e}", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Insufficient Permission", status=status.HTTP_401_UNAUTHORIZED)


    # The entire record needs to be sent to update a movie
    def put(self, request):
        if request.user.is_authenticated and request.user.username == 'admin':
            movie_obj = Movie.objects.filter(name=request.data.get('name'))
            if movie_obj:
                try:
                    movie_obj = movie_obj[0]
                    # if multiple records update the first one                
                    director_obj, _ = Director.objects.get_or_create(name=request.data.get('director'))

                    movie_obj.imdb_score = request.data.get('imdb_score')
                    movie_obj.popularity = request.data.get('99popularity')
                    movie_obj.director = director_obj
                    movie_obj.genre.clear()
                    for each_genre in request.data.get('genre'):
                        genre_obj, _ = Genre.objects.get_or_create(name=each_genre)
                        movie_obj.genre.add(genre_obj)
                    movie_obj.save()
                    return Response("Record updated successfully", status=status.HTTP_200_OK)
                except Exception as e:
                    return Response(f"Bad Record:{e}", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("No record found for the given movie name", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Insufficient Permission", status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        if request.user.is_authenticated and request.user.username == 'admin':
            movie_obj = Movie.objects.filter(name=request.data.get('name'))
            if movie_obj:
                try:
                    movie_obj = movie_obj[0]
                    # if multiple records delete the first one
                    movie_obj.delete()
                    return Response("Record deleted successfully", status=status.HTTP_200_OK)
                except Exception as e:
                    return Response(f"Failed to delete Record:{e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response("No record found for the given movie name", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Insufficient Permission", status=status.HTTP_401_UNAUTHORIZED)