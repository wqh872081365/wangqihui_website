# -*- coding: utf-8 -*-

from django import template
from django.utils import timezone
from blog.models import Article, Category
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta


register = template.Library()


@register.simple_tag()
def count_article(article_list):
    return article_list.count()
