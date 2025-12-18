from django.db import models
from user.models import User
from school.models import School
class Employee(models.Model):
    class RoleChoices(models.TextChoices):
        MANAGER = 'manager',
        MENTOR = 'mentor'

    user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True , blank=True )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(choices=RoleChoices.choices , max_length=50)
    school = models.ForeignKey(School , related_name='employee' , on_delete=models.CASCADE)

    class Meta:
        permissions =[('add_user_employee' , 'Can create user foe employee')]