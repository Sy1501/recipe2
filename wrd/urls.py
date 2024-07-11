from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('recipes', views.RecipeView.as_view(), name='recipes'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'), 
    path('accounts/', include('allauth.urls')),
    
      
]
