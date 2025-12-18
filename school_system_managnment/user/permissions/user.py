from permissions.customPermissionBase import CustomBasePermission
APPNAME = 'user'

class View_User(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Add_User(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Change_User(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Destroy_User(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
