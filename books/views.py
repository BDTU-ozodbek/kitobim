from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    query = request.GET.get('q')
    genre_id = request.GET.get('genre')

    book_list = Book.objects.all().order_by('-id')

    if query:
        book_list = book_list.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    if genre_id:
        book_list = book_list.filter(genres__id=genre_id)

    paginator = Paginator(book_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    genres = Genre.objects.all()

    return render(request, 'books/home.html', {
        'page_obj': page_obj,
        'query': query,
        'genres': genres
    })
def contact(request):
    return render(request, 'books/contact.html')

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def about(request):
    return render(request, 'books/about.html')
