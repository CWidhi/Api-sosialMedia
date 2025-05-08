from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from .permission import IsSelf

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
        
    def get_permissions(self):
        if self.request.method == 'GET' and self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated(), IsSelf()]

    def perform_update(self, serializer):
        serializer.save()

    def get_object(self):
        obj = super().get_object()
        if self.request.method not in ['GET']:
            if obj != self.request.user:
                raise PermissionDenied("You do not have permission to modify this user.")
        return obj

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []