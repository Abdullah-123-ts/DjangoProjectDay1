# Generated by Django 5.1.7 on 2025-03-20 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ClassBasedViewsBook", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="Published_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255)),
                ("bio", models.CharField(blank=True, max_length=255)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="books",
                        to="ClassBasedViewsBook.book",
                    ),
                ),
            ],
        ),
    ]
