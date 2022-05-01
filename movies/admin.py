from django.contrib import admin

from .models import Movie, MovieQuote

class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name',)

class MovieQuoteAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieQuote, MovieQuoteAdmin)
# Register your models here.
