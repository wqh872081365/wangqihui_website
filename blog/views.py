# -*- coding:utf-8 -*-
from django.shortcuts import render

# from django.views.generic import ListView, DetailView
from django.views.generic import View
from blog.models import Article, Category
import markdown2


class IndexView(View):

    def get(self, request):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list


class ArticleDetailView(View):

    def get(self, request):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body)
        return obj


class CategoryView(View):

    def get(self, request):
        # get_queryset 的作用已在第一篇中有介绍，不再赘述
        article_list = Article.objects.filter(category=self.kwargs['cate_id'],status='p')
        # 注意在url里我们捕获了分类的id作为关键字参数（cate_id）传递给了CategoryView，传递的参数在kwargs属性中获取。
        for article in article_list:
            article.body = markdown2.markdown(article.body, )
        return article_list

