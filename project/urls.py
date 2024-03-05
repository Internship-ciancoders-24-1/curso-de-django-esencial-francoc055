from django.contrib import admin
from django.urls import path
from project import views
from posts import views as posts_views

urlpatterns = [
    path('main', views.saludar),
    path('ordenar', views.ordenar),
    path('ordenar', views.ordenar),

    path('posts/', posts_views.list_posts),
]
