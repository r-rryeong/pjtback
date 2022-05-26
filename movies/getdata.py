import requests, json
from decouple import config

TMDB_API_KEY = config('TMDB_API_KEY')

def get_movie_data():
    total_data = []

    for i in range(1, 51):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:

            id = movie['id']
            req_url = f"https://api.themoviedb.org/3/movie/{id}/videos?api_key={TMDB_API_KEY}&language=ko-KR"
            movie_video = requests.get(req_url).json()

            if movie.get('release_date') and movie_video['results']:
                fields = {
                    'title': movie['title'],
                    'genres': movie['genre_ids'],
                    'release_date': movie['release_date'],
                    'vote_average': movie['vote_average'],
                    'popularity': movie['popularity'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'video': movie_video['results'][0]['key'],
                    'backdrop_path': movie['backdrop_path'],
                }

                data = {
                    "model": "movies.movie",
                    "pk": movie['id'],
                    "fields": fields,
                }

                total_data.append(data)

    with open("movies_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=3, ensure_ascii=False)

# get_movie_data()

def get_genre_data():
    genre_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            'name': genre['name']
        }
        data = {
            "model": "movies.genre",
            "pk": genre['id'],
            "fields": fields,
        }

        genre_data.append(data)

    with open("genres_data.json", "w", encoding="utf-8") as w:
        json.dump(genre_data, w, indent=3, ensure_ascii=False)

# get_genre_data()