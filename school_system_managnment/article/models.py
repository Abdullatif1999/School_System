from django.db import models
from material.models import Material , Media
class Article(Material):
    title = models.CharField(max_length=50)
    content = models.TextField()
