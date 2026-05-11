from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Если запрос безопасный (GET, HEAD, OPTIONS) - разрешаем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Если метод небезопасный (PUT, PATCH, DELETE) - проверяем автора
        return obj.author == request.user