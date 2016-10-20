# -*- coding: utf-8 -*-

from django import template
from django.utils import timezone
from blog.models import Article, Category, Tag
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta


register = template.Library()


@register.simple_tag()
def count_article(article_list):
    return article_list.count()


@register.simple_tag()
def tag_count_article(tag_id):
    return Article.objects.filter(tags=tag_id, status='p').count()


@register.simple_tag()
def category_count_article(category_id):
    return Article.objects.filter(category=category_id, status='p').count()

