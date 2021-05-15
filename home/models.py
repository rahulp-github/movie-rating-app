from django.db import models

# Create your models here.
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    movie_id = models.CharField(max_length=100)
    movie_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
