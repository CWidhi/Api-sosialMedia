from django.urls import path
from .views import LikeViewSet

like_view = LikeViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})

urlpatterns = [
    path('like/posts/<int:post_id>/likes/', like_view, name='post-likes'),
]
