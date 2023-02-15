from django import forms
from django.core.exceptions import ValidationError

from bibliotek.models import Readers


class ReadersForm(forms.ModelForm):
    class Meta:
        model = Readers
        fields = "__all__"

    def clean(self):
        activ_books = self.cleaned_data.get('activ_books')
        if activ_books.count() > 3:
            raise ValidationError('Maximum three categories are allowed.')

        return self.cleaned_data
