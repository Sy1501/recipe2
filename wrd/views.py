from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
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

class PostList(ListView):
    model = Recipe
    queryset = Recipe.objects.all()
    template_name = "index.html"
    






