from django.db import models

class School(models.Model):
    class TypeChoice(models.TextChoices):
        PRIMARY = 'primary'
        PREPARATORY  = 'preparatory'
        HIGH  = 'high'

    name = models.CharField(max_length=50 , unique=True)
    type = models.CharField(choices=TypeChoice.choices , max_length=50)
    

