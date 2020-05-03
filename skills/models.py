from django.db import models

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=300)
    class_name = models.CharField(max_length=300)
    width = models.IntegerField()