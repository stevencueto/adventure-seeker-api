from django.shortcuts import render, get_object_or_404
import json

# Create your views here.
from rest_framework import generics, permissions, viewsets,  parsers
from django.contrib.auth.models import User
from .serializers import PostSerializer
from django.core.serializers import serialize
from .models import Post
from django.http import HttpResponse


def upload_path(inance, filename):
    return '/'.join([])
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
    serializer_class = PostSerializer
    queryset = Post.objects.all()


    def update(self, instance, validated_data):
        liked_by = validated_data.pop('liked_by')
        for i in liked_by:
            instance.liked_by.add(i)
        instance.save()
        return instance


class UserPost(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by('id')


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class LikeView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Post.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending



    def update(sef,request,pk):
        user = request.user
        id=request.POST.get('id')
        post = Post.objects.get(id=int(pk))
        if user in post.liked_by.all():
            post.liked_by.remove(user)
        else:
            post.liked_by.add(user)
        data = serialize("json", [post])
        return HttpResponse(data, content_type="application/json")

