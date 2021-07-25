# Generated by Django 3.2.5 on 2021-07-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210724_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='books.BookGenre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='part_of_series',
            field=models.NullBooleanField(),
        ),
    ]
