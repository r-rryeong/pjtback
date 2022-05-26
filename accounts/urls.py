from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('mypick/<username>/', views.profile),
    path('user/', views.user_info),
]