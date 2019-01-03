from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=30)
    url = models.CharField(max_length=400)
    notes = models.CharField(max_length=160)

    def __str__(self):
        return self.name