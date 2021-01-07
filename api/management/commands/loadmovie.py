from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from api.models import Movie, Director, Genre

import multiline

def load_json(file_path):
    try:
        with open(file_path, 'r') as fp:
            return multiline.load(fp)
    except Exception as e:
        raise CommandError(e)

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--file_path', default=f'{settings.BASE_DIR}/imdb.json', help='Path of imdb json file')

    def handle(self, *args, **kwargs):
        movie_json = load_json(kwargs.get('file_path', ''))
        for each_movie in movie_json:
            try:
                director_obj, _ = Director.objects.get_or_create(name=each_movie.get('director'))
                # print(director_obj.name)
                each_movie_formatted = {
                    'name': each_movie.get('name'),
                    'imdb_score': each_movie.get('imdb_score'),
                    'popularity': each_movie.get('99popularity'),
                    'director': director_obj
                }
                movie_obj, _ = Movie.objects.get_or_create(**each_movie_formatted)
                # print(movie_obj)

                for each_genre in each_movie.get('genre'):
                    genre_obj, _ = Genre.objects.get_or_create(name=each_genre)
                    movie_obj.genre.add(genre_obj)
                movie_obj.save()

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Bad record: {each_movie} Skipping with error: {e}"))
                break

        self.stdout.write(self.style.SUCCESS(f"Successfully imported the data."))