from django.db import models

class Series(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    current = models.IntegerField()