from rest_framework import viewsets

from bibliotek.models import Author, Books, Readers
from bibliotek.serializers import AuthorSerializer, BooksSerializer, ReadersSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class ReadersViewSet(viewsets.ModelViewSet):
    queryset = Readers.objects.all()
    serializer_class = ReadersSerializer
