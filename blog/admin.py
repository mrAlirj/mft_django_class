from django.contrib import admin
from .models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'create_date', 'update_date')
    search_fields = ('title', 'body', 'author__email', 'author__mobile', 'author__first_name')
    list_filter = ('create_date', 'author__email')
    list_editable = ('title',)
    list_per_page = 4
    list_display_links = ('author', 'id')
    search_help_text = "insert in the input: title or body or author email"
    date_hierarchy = 'create_date'



@admin.register(Comment)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'create_date', 'update_date')
