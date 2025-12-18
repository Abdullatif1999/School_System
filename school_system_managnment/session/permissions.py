from permissions.customPermissionBase import CustomBasePermission
APPNAME = 'session'

class View_Session(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Add_Session(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Change_Session(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Destroy_Session(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name