from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'date', 'description')
    list_filter = ('tag', 'date')
    search_fields = ('title', 'description', 'content')
    date_hierarchy = 'date'
    ordering = ['-date']
