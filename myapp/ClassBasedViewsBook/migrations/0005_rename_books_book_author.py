# Generated by Django 5.1.7 on 2025-03-20 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ClassBasedViewsBook", "0004_rename_author_book_books"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="books",
            new_name="author",
        ),
    ]
