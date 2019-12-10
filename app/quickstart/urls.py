from django.urls import path
from . import views

urlpatterns = [
    path('users', views.UsersList.as_view(), name='users'),
    # ----- Book -----
    path('books', views.BookList.as_view(), name='books'),
    path('book/<int:pk>', views.BookGet.as_view(), name='book'),
    path('book', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete', views.BookDelete.as_view(), name='book-delete'),
    # ----- Author -----
    path('authors', views.AuthorList.as_view(), name='athors'),
    path('author/<int:pk>', views.AuthorGet.as_view(), name='author'),
    path('author', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete', views.AuthorDelete.as_view(), name='author-delete'),
    path('books_by_author/', views.BooksByAuthor.as_view(), name='books-by-author'),
    path('reserve_book', views.ReserveBook.as_view(), name='reserve-book')
]