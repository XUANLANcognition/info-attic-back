from django.contrib import admin

from .models import Book, BookQuote

class BookAmdin(admin.ModelAdmin):
    list_display = ('book_name',)

class BookQuoteAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(Book, BookAmdin)
admin.site.register(BookQuote, BookQuoteAdmin)
# Register your models here.
