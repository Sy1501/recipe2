from django.contrib import admin
from django.urls import path, include
from wrd.views import redirect_to_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  
    path('', redirect_to_login, name='home'),   
]
