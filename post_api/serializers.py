from rest_framework import serializers 
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Post # tell django which model to use
        fields = ('id', 'title', 'location','description', 'img', 'current_date', 'user', 'liked_by') # tell django which fields to include
        depth = 1

    
    def update(self, instance, validated_data):
        liked_by = validated_data.pop('liked_by')
        for i in liked_by:
            instance.liked_by.add(i)
        instance.save()
        return Response(data, status=status.HTTP_200_OK)

class SimplePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1



