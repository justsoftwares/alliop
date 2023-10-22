from typing import Container

from rest_framework import permissions


def get_permission_class(show_user_fields: Container, edit_user_fields: Container):
    class Permission(permissions.IsAuthenticated):
        def has_object_permission(self, request, view, obj):
            user = request.user
            if user in obj[edit_user_fields]:
                return True
            return (user in obj[show_user_fields] and request.method in permissions.SAFE_METHODS
                    or user.is_staff)

    return Permission
