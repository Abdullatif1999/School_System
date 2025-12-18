from django.db import models
from material.models import Material , Media

class Video(Material):
    title = models.CharField(max_length=200)
    media = models.OneToOneField(Media , related_name='video' , on_delete=models.CASCADE)
    