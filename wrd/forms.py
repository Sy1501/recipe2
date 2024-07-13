from django import forms
from .models import Comment, Recipe

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'method', 'excerpt']  
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 5}),
            'method': forms.Textarea(attrs={'rows': 10}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Recipe.objects.filter(slug=slug).exists():
            raise forms.ValidationError("A recipe with this slug already exists. Please choose a unique slug.")
        return slug

    def save(self, commit=True):
        instance = super(RecipeForm, self).save(commit=False)
        instance.status = 0  
        if commit:
            instance.save()
        return instance