from django.contrib import admin

from bibliotek.forms import ReadersForm
from bibliotek.models import Author, Readers, Books


class ReadersAdmin(admin.ModelAdmin):
    form = ReadersForm


admin.site.register(Readers, ReadersAdmin)
admin.site.register(Books)
admin.site.register(Author)

