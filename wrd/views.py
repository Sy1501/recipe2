from django.shortcuts import redirect, render, get_object_or_404
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


class RecipeView(ListView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipes'
    paginate_by = 2

    def get_queryset(self):
        return Recipe.objects.filter(status=1)

def recipe_detail(request, slug):
    
    
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    return render(request, "recipe_detail.html", {"recipe": recipe},)




