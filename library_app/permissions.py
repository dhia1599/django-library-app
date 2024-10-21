
from rest_framework import permissions

from library_app.models import BlacklistedToken

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='admin').exists()
    

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.groups.filter(name='lecteur').exists()
        return False
    
