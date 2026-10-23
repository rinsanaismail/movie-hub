from django.db import models

# Create your models here.
class Genre(models.Model):
     name = models.CharField(max_length=100)
     def __str__(self):
         return self.name 
class Language(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Movie(models.Model):
     movie_name = models.CharField(max_length=200)
     image = models.ImageField(upload_to='movies/', null=True, blank=True)
     genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, 
blank=True, related_name='movies') 
     director = models.CharField(max_length=200, null=True, blank=True) 
     description = models.TextField(null=True, blank=True) 
     released_year = models.PositiveIntegerField(null=True, blank=True) 
     collection = models.CharField(max_length=100, null=True, blank=True) 
     rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, 
blank=True) 
     actor = models.CharField(max_length=200, null=True, blank=True) 
     actress = models.CharField(max_length=200, null=True, blank=True) 
     language = models.ForeignKey(Language, on_delete=models.SET_NULL,
null=True, blank=True, related_name='movies') 
     created_at = models.DateTimeField(auto_now_add=True) 
     def __str__(self): return self.movie_name