# Generated by Django 3.2.5 on 2021-07-29 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20210729_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]