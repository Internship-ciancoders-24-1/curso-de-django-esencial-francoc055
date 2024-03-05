from django.contrib import admin
from django.urls import path
from project import views
from posts import views as posts_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main', views.saludar),
    path('ordenar', views.ordenar),
    path('ordenar', views.ordenar),

    path('posts/', posts_views.list_posts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
