# -*- coding:utf-8 -*-

from django.contrib import admin
from models import Article, Category, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "status", "abstract", "views", "likes", "topped", "category")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
