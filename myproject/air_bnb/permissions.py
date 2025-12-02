from rest_framework.permissions import BasePermission


class CheckPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'guest':
            return True
        else:
            return False


class CreatePropertyPermission(BasePermission):
    def has_permission(self, request, view):
       if request.user.role == 'host':
           return True
       else:
           return False
