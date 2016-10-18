# -*- coding:utf-8 -*-
from django.shortcuts import render

# from django.views.generic import ListView, DetailView
from django.views.generic import View
from blog.models import Article, Category
import markdown2


class IndexView(View):

    def get(self, request):
        article_list = Article.objects.filter(status='p')
        category_list = Category.objects.all()
        # for article in article_list:
        #     article.body = markdown2.markdown(article.body, )
        print article_list
        return render(request, "blog/index.html", {
            "article_list": article_list,
            "category_list": category_list,
        })


class ArticleDetailView(View):

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        # print article.title
        # article.body = markdown2.markdown(article.body)
        return render(request, "blog/detail.html", {
            "article": article,
        })


class CategoryView(View):

    def get(self, request, category_id):
        article_list = Article.objects.filter(category=category_id, status='p')
        category = Category.objects.get(id=category_id)
        # for article in article_list:
        #     article.body = markdown2.markdown(article.body, )
        return render(request, "blog/category.html", {
            "article_list": article_list,
            "category": category,
        })

