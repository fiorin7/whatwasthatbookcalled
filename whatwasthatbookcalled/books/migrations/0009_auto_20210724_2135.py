# Generated by Django 3.2.5 on 2021-07-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_part_of_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='additional_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_tips',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, to='books.BookGenre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='plot_details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='quotes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_read',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_written',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
