from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.movie_list, name='movie_list'), path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),]
from django.urls import path 
from . import views 
 
urlpatterns = [ 
   path('', views.movie_list, name='movie_list'), 
   path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),]
from django.urls import path 
from .views import MovieListView, MovieDetailView 
 
urlpatterns = [ 
   path("", MovieListView.as_view(), name="movie_list"), 
   path("movie/<int:pk>/", MovieDetailView.as_view(), 
name="movie_detail"),
]