from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if  request.user.is_staff == True and request.user.is_superuser == True:
            return True

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        if  request.user.is_staff == True and request.user.is_superuser == False:
            return True

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
         if  request.user.is_staff == False and request.user.is_superuser == False:
            return True