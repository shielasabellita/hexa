from django.db import models
from django.contrib.auth.models import User
from api.models.settings_model import Company


class Domain(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=120)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
