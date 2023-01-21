from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as authviews

urlpatterns = [
    path('create', views.post_create, name = 'create'),
    path('feed', views.feed, name = 'feed'),
    path('like', views.like_post, name = 'like'),
   
]
