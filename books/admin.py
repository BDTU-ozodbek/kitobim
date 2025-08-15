from django.contrib import admin
from .models import Book, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages')
    search_fields = ('title', 'author')
    list_filter = ('genres',)
    filter_horizontal = ('genres',)  # ko‘p janr tanlash uchun chiroyli UI
