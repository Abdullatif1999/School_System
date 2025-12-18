from django.db import models
from school.models import School
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager 
from django.core.validators import DecimalValidator
import uuid
from .validations import PhoneValidations
class UserManager(BaseUserManager):
    def create_user(self, email ,password ,**kwargs):
        
        email = self.normalize_email(email=email)
        if email:
            user = self.model(email=email , **kwargs)
            user.set_password(password)
            user.save(using = self.db)
            return user
        raise ValueError({"status":False , "error":"error in email address"})
    def create_superuser(self , email , password , **kwargs):
        kwargs.setdefault("is_staff" , True)
        kwargs.setdefault("is_superuser" , True)
        return self.create_user(email , password , **kwargs)


class User(AbstractBaseUser , PermissionsMixin):
    class CityChoices(models.TextChoices):
        HOMS = 'homs'
        DAMASCUS = 'damascus'
    
    id = models.UUIDField(primary_key=True , unique=True , default=uuid.uuid4)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100 , validators=[PhoneValidations()])
    email = models.EmailField(unique=True)
    city = models.CharField(choices=CityChoices.choices , max_length=30)
    school = models.ForeignKey(School , related_name='users' , on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name' , 'last_name' , 'phone' , 'city' , 'school']