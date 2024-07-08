from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at', 'updated_at')
    search_fields = ['title', 'author__username', 'ingredients', 'method']
    list_filter = ('status', 'created_at', 'author')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'method')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'approved', 'created_on')
    search_fields = ['author__username', 'body']
    list_filter = ('approved', 'created_on', 'author')
    summernote_fields = ('body',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)