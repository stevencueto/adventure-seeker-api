from django.db import models

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=30)
   location = models.CharField(max_length=50)
   description = models.CharField(max_length=350) 
   img = models.CharField(max_length=500) 
   current_date = models.DateField()
   user = models.CharField(max_length=20) 
   likes = models.IntegerField()