from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PostSerializer # tell django what serializer to use

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer