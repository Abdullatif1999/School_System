from django.db import models
from school.models import School


class Subject(models.Model):
    name = models.CharField(max_length=50)
    clas = models.ForeignKey('clas.Clas',related_name="subjects",on_delete=models.CASCADE , null=True , blank=True)
    school = models.ForeignKey(School , related_name='subject' , on_delete=models.CASCADE)