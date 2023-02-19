from django.shortcuts import render
from rest_framework import generics

from bibliotek.models import Author, Books, Readers
from bibliotek.serializers import AuthorSerializer, BooksSerializer, BooksListSerializer, BooksCreateSerializer, \
    AuthorCreateSerializer, AuthorListSerializer, ReadersCreateSerializer, ReadersListSerializer, ReadersSerializer


class AuthorCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    # model = Author
    serializer_class = AuthorCreateSerializer


class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    # model = Author
    serializer_class = AuthorSerializer


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    # model = Author
    serializer_class = AuthorListSerializer


class BooksCreateView(generics.CreateAPIView):
    queryset = Books.objects.all()
    # model = Books
    serializer_class = BooksCreateSerializer


class BooksView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    # model = Books
    serializer_class = BooksSerializer


class BooksListView(generics.ListAPIView):
    queryset = Books.objects.all()
    # model = Books
    serializer_class = BooksListSerializer


class ReadersCreateView(generics.CreateAPIView):
    queryset = Readers.objects.all()
    # model = Readers
    serializer_class = ReadersCreateSerializer


class ReadersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Readers.objects.all()
    # model = Readers
    serializer_class = ReadersSerializer


class ReadersListView(generics.ListAPIView):
    queryset = Readers.objects.all()
    # model = Readers
    serializer_class = ReadersListSerializer
