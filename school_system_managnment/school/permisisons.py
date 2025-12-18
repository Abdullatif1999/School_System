from rest_framework.permissions import BasePermission

class Retreive_School(BasePermission):
    def  has_object_permission(self, request, view, obj):
        if request and  request.user:
            if request.user.school == obj:
                    return True
        return False