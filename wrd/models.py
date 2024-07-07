from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(max_length=250, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")


  ingredients = models.TextField()
  method = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)
  excerpt = models.TextField(blank=True)

  def __str__(self):
    return self.title