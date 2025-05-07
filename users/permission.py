from rest_framework import permissions

class IsSelf(permissions.BasePermission):
    """
    Custom permission to only allow users to edit their own data.
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
