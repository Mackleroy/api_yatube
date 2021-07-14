from django_filters import rest_framework as filters
from .models import Post


class PostDateFilter(filters.FilterSet):
    min_date = filters.DateTimeFilter(field_name='pub_date', lookup_expr='gte')
    max_date = filters.DateTimeFilter(field_name='pub_date', lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['text', 'title']
