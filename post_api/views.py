from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, viewsets
from .serializers import PostSerializer
from .models import Post

class PostList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Post.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PostSerializer # tell django what serializer to use

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer


class UserPost(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.request.user.post.all().order_by('id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)