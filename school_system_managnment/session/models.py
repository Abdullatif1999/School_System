from django.db import models
from subject.models import Subject
from school.models import School
class Session(models.Model):
    school = models.ForeignKey(School , related_name='seassons' , on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject  , related_name='sessions' , on_delete=models.CASCADE , null=True , blank=True)
    title = models.CharField(max_length=200)
    time_from = models.TimeField()
    time_to = models.TimeField()