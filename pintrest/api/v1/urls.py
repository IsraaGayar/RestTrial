from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    # path('',views.hello_world, name='hellowolds' )
    path('movies/list',views.movie_index, name='mymovies' ),
    path('movies/create', views.movie_create, name='mycreatemovie'),
    path('movies/get/<int:id>', views.movie_details, name='mygetmovie'),
    path('movies/delete/<int:id>', views.movie_delete, name='mydelmovie'),
    path('movies/edit/<int:id>', views.movie_edit, name='myeditmovie'),
    # the bonus part
    path('movies/get/<int:id>/actors', views.movie_actors, name='myactorsmovie'),
    path('movies/actors', views.all_actors, name='myactors'),
]
