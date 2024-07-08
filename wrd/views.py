from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Recipe

class IndexView(TemplateView):
    template_name = 'wrd/index.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def redirect_to_login(request):
    return redirect(reverse('account_login'))

class RecipeListView(ListView):
    model = Recipe
    template_name = 'wrd/index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.filter(status=1)


