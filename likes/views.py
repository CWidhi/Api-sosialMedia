from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Like
from .serializer import LikeSerializer
from posts.models import Post

class LikeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, post_id=None):
        likes = Like.objects.filter(post_id=post_id)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def create(self, request, post_id=None):
        post = Post.objects.filter(id=post_id).first()
        if not post:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, post_id=None):
        like = Like.objects.filter(user=request.user, post_id=post_id).first()
        if not like:
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_404_NOT_FOUND)
        like.delete()
        return Response({'detail': 'Like removed.'}, status=status.HTTP_204_NO_CONTENT)
