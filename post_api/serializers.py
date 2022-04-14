from rest_framework import serializers 
from .models import Post 
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Post # tell django which model to use
        fields = ('id', 'title', 'location','description', 'img', 'current_date', 'user', 'likes') # tell django which fields to include