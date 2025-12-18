from permissions.customPermissionBase import CustomBasePermission
APPNAME = 'permission'

class View_Permission(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name