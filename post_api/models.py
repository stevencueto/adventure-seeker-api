from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=30)
   location = models.CharField(max_length=50)
   description = models.CharField(max_length=350) 
   img = models.CharField(max_length=500) 
   current_date = models.DateField(default=date.today)
   user = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE, null=True)
   likes = models.IntegerField()