from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Books(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(max_length=300, verbose_name='Описание')
    number_pages = models.IntegerField(verbose_name='Кол-во станиц')
    author = models.ManyToManyField(Author, help_text='Выберите автора книги',
                                    verbose_name='Автор')
    quantity = models.IntegerField(verbose_name='Кол-во книг в библиотеке')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']

    def __str__(self):
        return self.title


class Readers(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    phone = models.BigIntegerField(verbose_name='Номер телефона')
    status = models.BooleanField(default=True, verbose_name='Статус читателя')
    activ_books = models.ManyToManyField(Books, blank=True, verbose_name='Активные книги')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
