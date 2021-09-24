from rest_framework import routers

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, FollowViewSet, PostViewSet

VERSION_1 = 'v1/'

router_v1 = routers.DefaultRouter()
router_v1.register(VERSION_1 + r'posts', PostViewSet, basename='posts')
router_v1.register(VERSION_1 + r'groups', GroupViewSet, basename='groups')
router_v1.register(VERSION_1 + r'follow', FollowViewSet, basename='follow')
router_v1.register(
    VERSION_1 + r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path(VERSION_1, include('djoser.urls')),
    path(VERSION_1, include('djoser.urls.jwt')),
]
