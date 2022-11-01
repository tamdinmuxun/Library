from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Book


def index(request):
    return HttpResponse("Hello, world. You're at the library index.")


def books_list(request):
    latest_books_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_books_list': latest_books_list,
    }
    return render(request, 'library/index.html', context)


def book_info(request, book_id):
    # try:
    #     book = Book.objects.get(pk=book_id)
    # except Book.DoesNotExist:
    #     raise Http404("Book does not exist")
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/detail.html', {'book': book})
