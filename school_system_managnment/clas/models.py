from django.db import models
from school.models import School


class Clas(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School , related_name='clases' , on_delete=models.CASCADE)


