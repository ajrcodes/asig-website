from django.db import models

# Create your models here.
class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    letter = models.FileField(upload_to='uploads/')
