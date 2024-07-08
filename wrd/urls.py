from django.contrib import admin
from django.urls import path, include
from wrd.views import redirect_to_login
from . import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),  
    path('', redirect_to_login, name='home'),
    path('', views.PostList.as_view(), name='home'),   
]
