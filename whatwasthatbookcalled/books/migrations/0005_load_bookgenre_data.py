from django.db import migrations


def load_genres(apps, schema_editor):
    BookGenre = apps.get_model("books", "BookGenre")
    BookGenre(id=1, name="Action and Adventure").save()
    BookGenre(id=2, name="Classics").save()
    BookGenre(id=3, name="Comic Book").save()
    BookGenre(id=4, name="Mystery").save()
    BookGenre(id=5, name="Fantasy").save()
    BookGenre(id=6, name="Historical Fiction").save()
    BookGenre(id=7, name="Horror").save()
    BookGenre(id=8, name="Romance").save()
    BookGenre(id=9, name="Sci-Fi").save()
    BookGenre(id=10, name="Thriller").save()
    BookGenre(id=11, name="Biography").save()
    BookGenre(id=12, name="History").save()
    BookGenre(id=13, name="Memoir").save()
    BookGenre(id=14, name="Poetry").save()
    BookGenre(id=15, name="Self-Help").save()
    BookGenre(id=16, name="Non-fiction").save()


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_bookgenre"),
    ]
    operations = [
        migrations.RunPython(load_genres),
    ]
