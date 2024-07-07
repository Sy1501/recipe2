from django.contrib import admin
from .models import Recipe, Comment  # Ensure both models are imported

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Comment)