# Generated by Django 4.1.7 on 2023-02-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotek', '0003_alter_readers_activ_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readers',
            name='activ_books',
            field=models.ManyToManyField(to='bibliotek.books', verbose_name='Активные книги'),
        ),
    ]
