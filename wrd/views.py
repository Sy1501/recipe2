from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, TemplateView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm


def home(request):
    return render(request, 'index.html')       


class RecipeView(ListView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipes'
    paginate_by = 3

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


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.status = 0 
            recipe.save()
            messages.success(request, 'Your recipe has been added successfully and is awaiting approval.')
            return redirect('home')  # Redirect to home page
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})


def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user != recipe.author and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to edit this recipe.")
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.status = 0  
            recipe.save()
            messages.success(request, 'Your recipe has been updated and is awaiting approval.')
            return redirect('recipe_detail', slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})


def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user != recipe.author and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to delete this recipe.")
    
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Your recipe has been deleted.')
        return redirect('recipes')
    
    return render(request, 'delete_recipe.html', {'recipe': recipe})


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to edit this comment.")
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.approved = False  
            comment.save()
            messages.success(request, 'Your comment has been updated and is awaiting approval.')
            return redirect('recipe_detail', slug=comment.recipe.slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author and not request.user.is_staff:
        return HttpResponseForbidden("You don't have permission to delete this comment.")
    
    if request.method == 'POST':
        recipe_slug = comment.recipe.slug
        comment.delete()
        messages.success(request, 'Your comment has been deleted.')
        return redirect('recipe_detail', slug=recipe_slug)
    
    return render(request, 'delete_comment.html', {'comment': comment})