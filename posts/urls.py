from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter

from posts.views import *

router = DefaultRouter()
router.register('posts', PostViewSet, basename='Posts')
router.register('posts/<int:post_pk>/comments', CommentsViewSet, basename='comments')

# posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
# posts_router.register('comments', CommentsViewSet, basename='comments')
#
# comments_router = routers.NestedSimpleRouter(posts_router, r'comments', lookup='comment')
# comments_router.register('answers', AnswersViewSet, basename='answers')

urlpatterns = [
    path('api-token-auth/', ObtainAuthToken.as_view()),
    # path('', include(router.urls)),
    # path('', include(posts_router.urls)),
    # path('', include(comments_router.urls)),
]
