from django.db import models

# Create your models here.
class Certificates(models.Model):
    name = models.CharField(max_length=300)
    issuedby = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    description = models.TextField()
    cred_if = models.CharField(max_length=200)
    hyperlink = models.URLField()