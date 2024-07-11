from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, TemplateView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm


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
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()
    
    
    return render(
        request,
        "recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )




