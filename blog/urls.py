from django.urls import path
from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('posts', PostListAPIView.as_view(), name="posts"),
    path('posts/<str:slug>', PostDetailAPIView.as_view(), name="post")
]