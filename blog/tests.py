# -*- coding: utf-8 -*-

from django.test import TestCase
from django.http import HttpResponse

from blog.models import Article, Category, Tag


def test_add(request):
    # test1 = Category(name='d',)
    # test2 = Article(title='test', body='test', status='p', views=1, likes=1, category_id=1)
    # test3 = Tag(name='xywz', )
    t4 = Tag.objects.get(id=4)
    test4 = Article.objects.get(id=4)
    test4.tags.add(t4)
    test4.save()
    return HttpResponse("<p>数据添加成功！</p>")
