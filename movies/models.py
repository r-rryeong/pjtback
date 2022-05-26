from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre, related_name='movie_genres')
    release_date = models.CharField(max_length=20)
    vote_average = models.FloatField()
    popularity = models.IntegerField(null=True)
    overview = models.TextField()
    poster_path = models.TextField()
    video = models.TextField()
    backdrop_path = models.TextField(null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    is_watched = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watch_movie')


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')    # 필드명.reviews.all()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')    # 필드명.reviews.all()
    title = models.CharField(max_length=50)
    content = models.TextField()
    review_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comingsoon(models.Model):
    title = models.CharField(max_length=50)
    poster_path = models.TextField()
    d_day = models.IntegerField()


class Boxoffice(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.CharField(max_length=20)
    audience = models.CharField(max_length=20)
    poster_path = models.TextField()
    year = models.IntegerField()