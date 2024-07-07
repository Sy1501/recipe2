from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(max_length=200, unique=True)
  description = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  content = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title