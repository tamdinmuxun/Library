from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books_list),
    path('book/<int:book_id>/', views.book_info, name='book_info')
]