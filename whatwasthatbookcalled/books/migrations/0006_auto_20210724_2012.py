# Generated by Django 3.2.5 on 2021-07-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_load_bookgenre_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, to='books.BookGenre'),
        ),
    ]
