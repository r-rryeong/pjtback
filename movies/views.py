from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from accounts.models import User
from .models import Movie, Review, Comment, Comingsoon, Boxoffice
from .serializers.movie import MovieSerializer, MovieDetailSerializer, ComingsoonSerializer, BoxofficeSerializer
from .serializers.review import ReviewTitleSerializer, ReviewSerializer
from .serializers.comment import CommentSerializer


@api_view(['GET'])
def movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_popular(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-popularity')[:15]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_recently(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-release_date')[4:19]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_top_rated(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-vote_average')[:15]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# 크롤링한 data
@api_view(['GET'])
def comingsoon(request):
    if request.method == 'GET':
        comingsoon_movies = Comingsoon.objects.all()
        serializer = ComingsoonSerializer(comingsoon_movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# 감상여부
@api_view(['POST'])
def watch_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.is_watched.filter(pk=user.pk).exists():
        movie.is_watched.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.is_watched.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_list_create(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewTitleSerializer(reviews, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_update_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    if request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment_list_create(request, movie_pk, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=user)
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, movie_pk, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = review.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    if request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)


@api_view(['GET'])
def movie_genre(request, genre_pk):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-popularity')
        movies = movies.filter(genres=genre_pk)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# 크롤링한 data
@api_view(['GET'])
def boxoffice(request, year):
    if request.method == 'GET':
        boxoffice_movies = Boxoffice.objects.all().filter(year=year)
        serializer = BoxofficeSerializer(boxoffice_movies, many=True)
        return Response(serializer.data)


# movie recommendation
@api_view(['GET'])
def recommend(request, username):
    if request.method == 'GET':

        # user가 '좋아요'한 movie에 접근
        me = User.objects.get(username=username)
        like_movies = me.like_movies.all()
        # '좋아요'를 누른 영화가 있다면
        if like_movies:
            # '좋아요'한 movie의 genre에 접근
            like_genres = []
            for movie in like_movies:
                for genre in movie.genres.all():
                    like_genres.append(genre.id)

            # 가장 선호하는 장르
            genre = {}
            cnt_lst = []
            for l_g in like_genres:
                cnt = like_genres.count(l_g)
                cnt_lst.append(cnt)
                genre[cnt] = l_g      # 같은 cnt가 있으면 마지막에 넣은 장르의 id가 key값으로 저장
                pick_genre = genre.get(max(cnt_lst))

            # 장르 기반 영화 10개
            movies = Movie.objects.all().filter(genres=pick_genre)
            movies1 = movies.all().order_by('?')[:10]
            # random 5개
            movies2 = Movie.objects.all().order_by('?')[:5]
            movie_set = movies1 | movies2     # queryset 합치기
            movie_set = movie_set.all().order_by('-popularity')
        
        # '좋아요'를 누른 영화가 없다면 랜덤으로 추천
        else:
            movie_set = Movie.objects.all().order_by('?')[:15]
            movie_set = movie_set.all().order_by('-popularity')
        
        serializer = MovieSerializer(movie_set, many=True)
        return Response(serializer.data)
