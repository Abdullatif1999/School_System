from rest_framework.permissions import BasePermission
class CustomBasePermission(BasePermission):
    def get_permission_name(self):
        pass

    def custom_condition(self):
        return True
    def has_permission(self, request, view):
        if request and  request.user:
            print(self.get_permission_name())
            return request.user.has_perm(self.get_permission_name()) and self.custom_condition()