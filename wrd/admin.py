from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at', 'updated_at')
    search_fields = ['title', 'author__username', 'ingredients', 'method']
    list_filter = ('status', 'created_at', 'author')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'method')
    list_editable = ('status',)  

    def save_model(self, request, obj, form, change):
        if not change:  
            obj.status = 0  
        super().save_model(request, obj, form, change)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'approved', 'created_on')
    search_fields = ['author__username', 'body']
    list_filter = ('approved', 'created_on', 'author')
    summernote_fields = ('body',)
    list_editable = ('approved',)  

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"