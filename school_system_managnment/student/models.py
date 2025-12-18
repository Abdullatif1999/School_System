from django.db import models
from user.models import User
from clas.models import Clas
from material.models import Material
from school.models import School
class Student(models.Model):
    user = models.OneToOneField(User , related_name='student' , on_delete=models.CASCADE , null=True , blank=True)
    date_of_birth = models.DateField()
    clas = models.ForeignKey(Clas , related_name='students' , on_delete=models.CASCADE)
    materials = models.ManyToManyField(Material , through="Student_Material" , related_name='students' , null=True , blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school = models.ForeignKey(School , related_name='student' , on_delete=models.CASCADE , default=1)
    class Meta:
        permissions = [('add_user_student' , 'Can add user for student')]

class Student_Material(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    material = models.ForeignKey(Material , on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)