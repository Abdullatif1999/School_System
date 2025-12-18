from django.db import models
from user.models import User
from subject.models import Subject
from school.models import School
class Teacher(models.Model):
    class SpecializationChoice(models.TextChoices):
        CA = 'ca'
        PH = 'ph'
        MA = 'ma'
    user = models.OneToOneField(User , related_name='teacher' , on_delete=models.CASCADE , null=True , blank=True)
    specialization = models.CharField(max_length=50 , choices=SpecializationChoice.choices)
    subjects = models.ManyToManyField(Subject , through="Teacher_Subject" , related_name='teachers')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school = models.ForeignKey(School , related_name='teacher' , on_delete=models.CASCADE )

    class Meta:
        permissions = [('add_user_teacher' , 'Can add user for teacher')]

        
class Teacher_Subject(models.Model):
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher , on_delete=models.CASCADE)
    class Meta:
        unique_together = ['teacher', 'subject']