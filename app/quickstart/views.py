from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class UsersList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# ----- Book -----

class BookList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookGet(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

class BookUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ----- Author -----

class AuthorList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorGet(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AuthorSerializer

class AuthorUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BooksByAuthor(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    
    def get_queryset(self):
        id_author = self.request.query_params.get('id_author', None)
        print(id_author)
        author = Author.objects.filter(pk=id_author)[0]
        return author.books.all()