
from django.shortcuts import render 
def movie_list(request): 
    return render(request, 'movie_list.html') 
def movie_detail(request, pk): 
    return render(request, 'movie_detail.html')
from django.views.generic import ListView, DetailView 
from .models import Movie 
 
 
class MovieListView(ListView): 
   model = Movie 
   template_name = "movie_list.html" 
   context_object_name = "movies" 
 
   def get_queryset(self): 
       queryset = Movie.objects.select_related( 
           "language", "genre" 
       ).order_by("-created_at") 
 
       search = self.request.GET.get("search") 
       language = self.request.GET.get("language") 
       genre = self.request.GET.get("genre") 
 
       if search: 
           queryset = queryset.filter(movie_name__icontains=search) 
 
       if language: 
           queryset = queryset.filter(language_id=language) 
 
       if genre: 
           queryset = queryset.filter(genre_id=genre) 
 
       return queryset 
 
   def get_context_data(self, **kwargs): 
       context = super().get_context_data(**kwargs) 
 
       from .models import Language, Genre 
 
       context["languages"] = Language.objects.all() 
       context["genres"] = Genre.objects.all() 
 
       context["selected_language"] = self.request.GET.get("language", "") 
       context["selected_genre"] = self.request.GET.get("genre", "") 
       context["search"] = self.request.GET.get("search", "") 
 
       return context 
 
 
class MovieDetailView(DetailView): 
   model = Movie 
   template_name = "movie_detail.html" 
   context_object_name = "movie"