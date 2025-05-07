from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('comment/', include(router.urls)),
]
