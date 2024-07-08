from django.contrib import admin
from django.urls import path, include
from wrd.views import redirect_to_login
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='post-list'), 
    path('accounts/', include('allauth.urls')),  
]
