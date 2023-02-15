from django.contrib import admin

from bibliotek.models import Author, Readers, Books


admin.site.register(Author)
admin.site.register(Readers)
admin.site.register(Books)
