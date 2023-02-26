from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from bibliotek.models import Author, Books, Readers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'photo', 'created_at', 'updated_at')


class BooksSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        slug_field='last_name',
        many=True
    )

    class Meta:
        model = Books
        fields = ('id', 'title', 'description', 'number_pages', 'author', 'quantity', 'created_at', 'updated_at')
        read_only_fields = ['author']


class ReadersSerializer(serializers.ModelSerializer):
    activ_books = serializers.SlugRelatedField(
        queryset=Books.objects.all(),
        slug_field='title',
        many=True
    )

    class Meta:
        model = Readers
        fields = ('id', 'first_name', 'last_name', 'phone', 'status', 'activ_books', 'created_at', 'updated_at')

