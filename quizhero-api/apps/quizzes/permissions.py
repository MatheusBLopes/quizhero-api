from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdmindOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user.is_staff and request.user)
