from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        if (not request.user.is_authenticated or request.method
           in permissions.SAFE_METHODS):
            return True
        return (obj.author == request.user)
