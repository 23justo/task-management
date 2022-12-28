from rest_framework import permissions

class UpdateOwnProjects(permissions.BasePermission):
    """only allow owner to update a project"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user.id == request.user.id

