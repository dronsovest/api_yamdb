from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    """
    Разрешен метод 'GET' для всех пользователей.
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Доступ разрешен администратору.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
                request.user.is_staff or request.user.role == "admin")

    def has_object_permission(self, request, view, obj):
        return (request.user.is_staff or request.user.role == "admin")
