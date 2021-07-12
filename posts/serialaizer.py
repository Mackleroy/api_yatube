from rest_framework import serializers

from posts.models import Post, Comment, Answer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'text', 'image', 'pub_date')
        read_only_fields = ['published_date']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ['author', 'post','created']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'author',
                  'comment',
                  'text', 'created')
        read_only_fields = ['author', 'created']
