from rest_framework import permissions


class IsAdmindOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or request.user.is_staff and request.user)
