from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

from posts.views import *

router = DefaultRouter()
router.register('posts', PostViewSet, basename='Posts')

urlpatterns = [
    path('api-token-auth/', ObtainAuthToken.as_view())
]

urlpatterns += router.urls
