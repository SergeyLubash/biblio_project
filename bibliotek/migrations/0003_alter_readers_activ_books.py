# Generated by Django 4.1.7 on 2023-02-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotek', '0002_alter_books_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readers',
            name='activ_books',
            field=models.ManyToManyField(max_length=3, to='bibliotek.books', verbose_name='Активные книги'),
        ),
    ]