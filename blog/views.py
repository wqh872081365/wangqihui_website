# -*- coding:utf-8 -*-
from django.shortcuts import render

# from django.views.generic import ListView, DetailView
from django.views.generic import View
from blog.models import Article, Category, Tag
import markdown2


class IndexView(View):

    def get(self, request):
        article_list = Article.objects.filter(status='p')
        category_list = Category.objects.all()
        # for article in article_list:
        #     article.body = markdown2.markdown(article.body, )
        article_number = article_list.count()
        tag_list = Tag.objects.all()
        return render(request, "blog/index.html", {
            "article_list": article_list,
            "category_list": category_list,
            "article_number": article_number,
            "tag_list": tag_list,
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
        article_number = article_list.count()
        # for article in article_list:
        #     article.body = markdown2.markdown(article.body, )
        return render(request, "blog/category.html", {
            "article_list": article_list,
            "category": category,
            "article_number": article_number,
        })


class TagView(View):

    def get(self, request, tag_id):
        article_list = Article.objects.filter(tags=tag_id, status='p')
        tag = Tag.objects.get(id=tag_id)
        article_number = article_list.count()
        # for article in article_list:
        #     article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return render(request, "blog/tag.html", {
            "article_list": article_list,
            "tag": tag,
            "article_number": article_number,
        })
