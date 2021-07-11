from rest_framework import viewsets, status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from posts.models import Post, Comment, Answer
from posts.serialaizer import PostSerializer, CommentSerializer, AnswerSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = Post.objects.get(id=pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)


class CommentsViewSet(viewsets.ViewSet):
    serializer_class = CommentSerializer

    def list(self, request, post_pk=None):
        queryset = Comment.objects.filter(post=post_pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, post_pk=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=Post.objects.get(pk=post_pk))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, post_pk=None):
        queryset = Comment.objects.filter(pk=pk, post=post_pk)
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None, post_pk=None):
        queryset = Comment.objects.filter(pk=pk, post=post_pk)
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, post_pk=None):
        queryset = Comment.objects.filter(pk=pk, post=post_pk)
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, post_pk=None):
        queryset = Comment.objects.filter(pk=pk, post=post_pk)
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_200_OK)


class AnswersViewSet(viewsets.ViewSet):
    serializer_class = AnswerSerializer

    def list(self, request, comment_pk=None, post_pk=None):
        queryset = Answer.objects.filter(comment=comment_pk)
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, comment_pk=None, post_pk=None):
        queryset = Answer.objects.filter(pk=pk, comment=comment_pk)
        comment = get_object_or_404(queryset, pk=pk)
        serializer = AnswerSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)