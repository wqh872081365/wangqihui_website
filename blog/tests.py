# -*- coding: utf-8 -*-

from django.test import TestCase
from django.http import HttpResponse

from blog.models import Article, Category


def test_add(request):
    # test1 = Category(name='1',)
    test2 = Article(title='test', body='test', status='p', views=1, likes=1)
    test2.save()
    return HttpResponse("<p>数据添加成功！</p>")
