from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField()
    description = models.TextField()
    cover = models.ImageField(upload_to='book_covers/', default='book_covers/default.jpg')
    genres = models.ManyToManyField(Genre, related_name='books')  # bir nechta janr

    def __str__(self):
        return self.title
