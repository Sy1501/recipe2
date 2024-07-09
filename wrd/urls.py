from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('recipes', views.RecipeView.as_view(), name='recipes'), 
    path('accounts/', include('allauth.urls')),
    
      
]
