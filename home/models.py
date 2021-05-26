from django.db import models
# Create your models here.
from django.contrib.auth.models import User
# Model For Comments
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    comment = models.CharField(max_length=200,null=True)
    movie_id = models.CharField(max_length=100,null=True)
    movie_name = models.CharField(max_length=100,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    time = models.TimeField(auto_now_add=True,null=True)

class WatchList(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=20)
    movie_name = models.CharField(max_length=100,null=True)
    movie_year = models.CharField(max_length=50,null=True)
    
