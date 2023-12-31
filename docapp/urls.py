from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('auth/login', views.login_user, name='login'),
    path('auth/logout', views.logout_user, name='logout'),
    path('auth/register', views.register_user, name='register_user'),
    path('', views.index, name='index'),
    path('summarize/', views.summarization, name='summarization'),
]
