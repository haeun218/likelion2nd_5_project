from django.shortcuts import render

from .models import Post
from .serializer import PostSerializer

# from django.http import Http404
from rest_framework import viewsets #왜?

"""
from rest_framework.response import Response
from rest_framework import status #어떤식으로 status를 받고 response를 시킬지 직접 설정해주기 위해

from rest_framework.views import APIView
"""
# Create your views here.

# CBV
# class 뭐뭐뭐(APTView):
    # def<내가_필요로_하는_HTTP_METHOD>
    # : 그 Http Method로 어떻게 처리할 지는 직접 정의

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# APIView

"""
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all() # 객체들의 목록 쿼리셋으로
        serializer = PostSerializer(posts, many=True) # 다수의 쿼리셋(객체)을 serialize시켜줄 때(넘길때) (many=True인자)
        return Response(serializer.data) # 직접 Response 리턴해주기 : serializer.data -> 이걸 직접 설정해주는 거임.

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PostList 클래스와는 달리 pk값을 받음(메소드에 pk인자)
class PostDetail(APIView):
    # get_object_or_404를 구현해주는 helper function
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk) # post = get_object_or_404(Post, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk) # post = get_object_or_404(Post, pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""