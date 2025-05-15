from django.shortcuts import render
from .models import Post

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    