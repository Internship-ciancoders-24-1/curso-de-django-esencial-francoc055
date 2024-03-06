from django.contrib import admin
from django.urls import path, include
from project import views
from posts import views as posts_views
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main', views.saludar, name='hello'),
    path('ordenar', views.ordenar, name='sort'),

    #posts
    path('posts/', posts_views.list_posts, name='feed'),

    #users
    path('users/login', users_views.login_view, name='login'),
    path('users/logout', users_views.logout_view, name='logout'),
    path('users/signup', users_views.signup, name='signup'),
    path('users/me/profile', users_views.update_profile, name='update_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
