from django.db import models


# Create your models here.
class Story(models.Model):
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.text
