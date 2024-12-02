from django.contrib import admin
from .models import Movie, Director

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'director', 'length', 'rating')  
    search_fields = ('title', 'director')  
    list_filter = ('year', 'rating')  
    ordering = ('year',) 


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

