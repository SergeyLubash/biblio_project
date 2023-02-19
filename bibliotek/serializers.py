from rest_framework import serializers

from bibliotek.models import Author, Books, Readers


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        read_only_fields = ("id", "first_name", "last_name", "photo")
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ("id", "first_name", "last_name", "photo")


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BooksCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        read_only_fields = ("id", "title", "description", "number_pages", "author", "quantity")
        fields = "__all__"


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"
        read_only_fields = ("id", "title", "description", "number_pages", "author", "quantity")


class BooksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class ReadersCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Readers
        read_only_fields = ("id", "first_name", "last_name", "phone", "status", "activ_books")
        fields = "__all__"


class ReadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readers
        fields = "__all__"
        read_only_fields = ("id", "first_name", "last_name", "phone", "status", "activ_books")


class ReadersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readers
        fields = "__all__"