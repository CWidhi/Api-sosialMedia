import os
from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser

def delete_file(file_field):
    """Helper function to delete file from storage if it exists."""
    if file_field and os.path.isfile(file_field.path):
        os.remove(file_field.path)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_delete=False).order_by('-created_at')  
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser] 
    permission_classes = [IsAuthenticatedOrReadOnly] 

    def get_queryset(self):
        return Post.objects.filter(is_delete=False).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if self.request.method not in ['GET']: 
            if obj.author != self.request.user:
                raise PermissionDenied("You do not have permission to modify this post.")
        return obj
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        delete_file(instance.img)
        return super().destroy(request, *args, **kwargs)
