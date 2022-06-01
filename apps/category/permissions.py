from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsAdminOrAllowAny(BasePermission):
    def has_permission(self,request,view):
        if request.method in SAFE_METHODS: #Get option head
            return True
        return bool(request.user and request.user.is_staff)
