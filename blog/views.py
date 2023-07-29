from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Post
from .serializers import PostSerializer, UserSerializer


class PostListAPIView(generics.ListAPIView):

    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
    
class PostDetailAPIView(generics.GenericAPIView):

    serializer_class = PostSerializer

    def get(self, request, slug):

        query_set = Post.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)
        
        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)
    

