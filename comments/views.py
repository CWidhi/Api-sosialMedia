from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(author=self.request.user, post_id=post_id)

    def perform_update(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(post_id=post_id)

    def get_object(self):
        obj = super().get_object()
        if self.request.method not in ['GET']: 
            if obj.author != self.request.user:
                raise PermissionDenied("You do not have permission to modify this comment.")
        return obj
