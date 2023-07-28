from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostListAPIView(generics.ListAPIView):

    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()