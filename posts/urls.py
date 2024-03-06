from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.PostsFeedView.as_view(), name='feed'),
    path('posts/new', views.create_post, name='create_post')
]
