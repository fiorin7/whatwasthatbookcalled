# Generated by Django 3.2.5 on 2021-08-01 22:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_alter_book_filled_fields_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='filled_fields_count',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(11)]),
        ),
    ]
