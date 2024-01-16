from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path



urlpatterns = [
    # Other URL patterns for your app
    # path('create_and_download/', create_and_download_file, name='create_and_download_file'),
    path('auth/login', views.login_user, name='login'),
    path('auth/logout', views.logout_user, name='logout'),
    path('auth/register', views.register_user, name='register_user'),
    path('', views.index, name='index'),
    path('summarize/', views.summarization, name='summarization'),
    path('spelling/', views.spelling, name='spelling'),
    path('create_and_download_file/', views.create_and_download_file, name='create_and_download_file'),
]
