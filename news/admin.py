from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Column, Article


class ColumnAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'intro', 'nav_display', 'home_display',)


class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time',)


admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
