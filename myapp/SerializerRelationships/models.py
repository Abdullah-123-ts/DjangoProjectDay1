from django.db import models

class Author2(models.Model):
    name            = models.CharField(max_length=255, blank=True)
    bio             = models.CharField(max_length=255, blank=True)
    date_of_birth   = models.DateField(null=True, blank=True)


class Book2(models.Model):
    title           = models.CharField(max_length=255, blank=True, unique=True)
    author          = models.ForeignKey(Author2,on_delete=models.CASCADE, related_name="books")
    Published_date  = models.DateField(null=True, blank=True)


class Genre(models.Model):
    book = models.ManyToManyField(Book2, related_name="genre")
    name       = models.CharField(max_length=255, blank=True)

