from django.db import models
from material.models import Material
class Quiz(Material):
    question = models.TextField()
    


class Option(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz , related_name='options' , on_delete=models.CASCADE)
    is_success = models.BooleanField(default=False)
