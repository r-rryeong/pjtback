from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # movies
    path('', views.movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('popular/', views.movie_popular),         # 인기 영화
    path('recently/', views.movie_recently),       # 최신 영화
    path('top_rated/', views.movie_top_rated),     # 평점 높은 영화
    path('comingsoon/', views.comingsoon),         # 개봉예정 영화
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/watch/', views.watch_movie),
    path('genre/<int:genre_pk>/', views.movie_genre),   # 장르별
    path('boxoffice/<int:year>/', views.boxoffice),     # 박스오피스
    # recommend
    path('recommend/<username>/', views.recommend),
    # reviews
    path('<int:movie_pk>/reviews/', views.review_list_create),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail_update_delete),
    # comments
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/', views.comment_list_create),
    path('<int:movie_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>/', views.comment_detail_update_delete),
]