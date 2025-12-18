from permissions.customPermissionBase import CustomBasePermission
APPNAME = 'teacher'

class View_Teacher(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Add_Teacher(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Change_Teacher(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Destroy_Teacher(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Add_User_Teacher(CustomBasePermission):
    global APPNAME
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name