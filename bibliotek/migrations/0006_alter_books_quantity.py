# Generated by Django 4.1.7 on 2023-02-17 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotek', '0005_alter_readers_activ_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='quantity',
            field=models.IntegerField(blank=True, verbose_name='Кол-во книг в библиотеке'),
        ),
    ]
