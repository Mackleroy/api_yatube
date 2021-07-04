from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'image', 'pub_date')
        read_only_fields = ['author', 'published_date']
