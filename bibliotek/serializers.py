from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from bibliotek.models import Author, Books, Readers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'photo', 'created_at', 'updated_at')


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id', 'title', 'description', 'number_pages', 'author', 'quantity', 'created_at', 'updated_at')


class ReadersSerializer(serializers.ModelSerializer):
    activ_books = SlugRelatedField(
        slug_field='title', many=True, queryset=Books.objects.all()
    )

    class Meta:
        model = Readers
        fields = ("id", "first_name", "last_name", "phone", "status", "activ_books", "created_at", "updated_at")
