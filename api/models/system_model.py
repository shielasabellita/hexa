from django.db import models

class Series(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    no_of_zeroes = models.IntegerField(default=5)
    current = models.IntegerField()


class DeletedDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_name = models.CharField(max_length=120, blank=True)
    id_no = models.CharField(max_length=120, blank=True)
    object = models.CharField(max_length=5000, blank=True)
    deleted_at = models.DateTimeField(auto_now=True)
    deleted_by = models.CharField(max_length=120)