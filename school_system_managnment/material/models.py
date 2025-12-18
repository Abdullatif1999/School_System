from django.db import models
from session.models import Session
from school.models import School
from polymorphic.models import PolymorphicModel

class Material(PolymorphicModel):
    session = models.ForeignKey(Session , related_name='materials' , on_delete=models.CASCADE)
    school = models.ForeignKey(School  , related_name='materials' , on_delete=models.CASCADE)



class Media(models.Model):
    # file = models.FileField(upload_to="image")
    file = models.URLField()