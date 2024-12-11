from django.db import models


# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=100, unique=True, default='name')
    reg_date = models.DateField()
    text = models.CharField(max_length=2000)
