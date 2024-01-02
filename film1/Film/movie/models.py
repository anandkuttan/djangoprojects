from django.db import models

# Create your models here.

class Movie(models.Model):
    cover=models.ImageField(upload_to="movie/cover",null=True,blank=True)
    name=models.CharField(max_length=20)
    des=models.CharField(max_length=20)
    year=models.IntegerField()