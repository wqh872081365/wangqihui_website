# -*- coding: utf-8 -*-

from django.test import TestCase
from django.http import HttpResponse

from blog.models import Article, Category, Tag


def test_add(request):
    # test1 = Category(name='d',)
    test2 = Article(title='wang', body='wang', status='3', views=1, likes=1, category_id=4)
    # test3 = Tag(name='xywz', )

    # t4 = Tag.objects.get(id=4)
    # test4 = Article.objects.get(id=4)
    # test4.tags.add(t4)

    # test5 = Article(title='test5', body='test5', status='p', views=1, likes=1, category_id=2)
    # test5.save()
    # test5.tags.add(Tag.objects.get(id=3))
    test2.save()
    return HttpResponse("<p>数据添加成功！</p>")
