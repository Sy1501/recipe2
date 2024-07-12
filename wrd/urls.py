from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('recipes', views.RecipeView.as_view(), name='recipes'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'), 
    path('edit-recipe/<slug:slug>/', views.edit_recipe, name='edit_recipe'),
    path('delete-recipe/<slug:slug>/', views.delete_recipe, name='delete_recipe'),
    path('edit-comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('accounts/', include('allauth.urls')),
]