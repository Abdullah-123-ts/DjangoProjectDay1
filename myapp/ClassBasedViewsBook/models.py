from django.db import models

class Author(models.Model):
    name            = models.CharField(max_length=255, blank=True)
    bio             = models.CharField(max_length=255, blank=True)
    date_of_birth   = models.DateField(null=True, blank=True)


class Book(models.Model):
    title           = models.CharField(max_length=255, blank=True, unique=True)
    # author          = models.CharField(max_length=255, blank=True, unique=True)
    author          = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    Published_date  = models.DateField(null=True, blank=True)




