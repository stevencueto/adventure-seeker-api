from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=30)
     location = models.CharField(max_length=50)
     description = models.CharField(max_length=350) 
     img = models.ImageField(null=True, blank=True, upload_to='media/') 
     current_date = models.DateTimeField(auto_now_add=True, null=True)
     user = models.ForeignKey(
        User, related_name="post", on_delete=models.CASCADE, null=True)
     liked_by = models.ManyToManyField(User, default=None, blank=True, related_name="liked_post")
