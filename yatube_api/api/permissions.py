from rest_framework import permissions


class OwnershipPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
        )

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            or request.method in permissions.SAFE_METHODS
        )
