from django.db import models

class Book(models.Model):
    title           = models.CharField(max_length=255, blank=True, unique=True)
    author          = models.CharField(max_length=255, blank=True, unique=True)
    Published_date  = models.DateTimeField(null=True, blank=True)
