from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Book, Author


def index(request):
    return HttpResponse("Hello, world. You're at the library index.")


class AuthorDatailView(DetailView):
    model = Author
    template_name = "library/author_detail.html"


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'birth_date']


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'birth_date']


# class BookListView(ListView):
#     model = Book
#     latest_books_list = Book.objects.order_by('-pub_date')[:5]
#     template_name = 'library/index.html'
#     paginate_by = 20
#
#     def get_ordering(self):
#         return 'title'


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/detail.html'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'pub_date']


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'pub_date']


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('books:books_list')


def books_list(request):
    latest_books_list = Book.objects.order_by('-pub_date')
    context = {
        'latest_books_list': latest_books_list,
    }
    return render(request, 'library/index.html', context)


# def book_info(request, book_id):
#     # try:
#     #     book = Book.objects.get(pk=book_id)
#     # except Book.DoesNotExist:
#     #     raise Http404("Book does not exist")
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, 'library/detail.html', {'book': book})
