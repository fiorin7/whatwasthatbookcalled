# Generated by Django 3.2.5 on 2021-07-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='part_of_series',
            field=models.BooleanField(blank=True, choices=[(None, "Can't remember"), (True, 'Yes'), (False, 'No')], null=True),
        ),
    ]
