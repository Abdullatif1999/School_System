from permissions.customPermissionBase import CustomBasePermission
APPNAME = 'student'

class View_Student(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Add_Student(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Add_User_Student(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Change_Student(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name
    
class Destroy_Student(CustomBasePermission):
    global APPNAME    
    def get_permission_name(self):
        name = f"{APPNAME}.{str(type(self).__name__).lower()}"
        return name