from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=300)
    madein = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    description = models.TextField()
    hyperlink = models.URLField()