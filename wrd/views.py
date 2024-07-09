from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Recipe


# class IndexView(TemplateView):
#     model = Recipe
#     template_name = 'index.html'
#     context_object_name = 'recipes'

#     def get_queryset(self):
#         return Recipe.objects.filter(status=1)

def home(request):
    return render(request, 'index.html')       

class RecipeView(View):
    
    def get(self, request):
        """ get request """
        recipes = Recipe.objects.filter(status=1)
        context = {
            "recipes": recipes,
        }
        return render(request, 'recipe.html', context)





