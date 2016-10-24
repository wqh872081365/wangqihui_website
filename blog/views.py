# -*- coding:utf-8 -*-
from django.shortcuts import render

# from django.views.generic import ListView, DetailView
from django.views.generic import View
from blog.models import Article, Category, Tag
import markdown2


class IndexView(View):

    def get(self, request):
        article_list = Article.objects.filter(status='p').order_by('-last_modified_time')
        articles = []
        for article in article_list:
            article_tags = article.tags.all()
            articles.append({"article": article, "article_tags": article_tags, })
            # print article_tags
        category_list = Category.objects.all().order_by('-last_modified_time')
        article_number = article_list.count()
        tag_list = Tag.objects.all().order_by('-last_modified_time')
        date_archive = Article.objects.archive()
        return render(request, "blog/index.html", {
            "articles": articles,
            "category_list": category_list,
            "article_number": article_number,
            "tag_list": tag_list,
            "date_archive": date_archive,
        })


class ArticleDetailView(View):

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        article_tags = article.tags.all()
        # print article.title
        # article.body = markdown2.markdown(article.body)
        return render(request, "blog/detail.html", {
            "article": article,
            "article_tags": article_tags,
        })


class CategoryView(View):

    def get(self, request, category_id):
        article_list = Article.objects.filter(category=category_id, status='p').order_by('-last_modified_time')
        articles = []
        for article in article_list:
            article_tags = article.tags.all()
            articles.append({"article": article, "article_tags": article_tags, })
        category = Category.objects.get(id=category_id)
        article_number = article_list.count()
        # for article in article_list:
        #     article.body = markdown2.markdown(article.body, )
        return render(request, "blog/category.html", {
            "articles": articles,
            "category": category,
            "article_number": article_number,
        })


class TagView(View):

    def get(self, request, tag_id):
        # article_list = Article.objects.filter(tags=tag_id, status='p')
        tag = Tag.objects.get(id=tag_id)
        article_list = tag.article_set.all().filter(status='p').order_by('-last_modified_time')
        articles = []
        for article in article_list:
            article_tags = article.tags.all()
            articles.append({"article": article, "article_tags": article_tags, })
        # print article_list
        article_number = article_list.count()
        # for article in article_list:
        #     article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return render(request, "blog/tag.html", {
            "articles": articles,
            "tag": tag,
            "article_number": article_number,
        })


class ArchiveView(View):

    def get(self):
        # 接收从url传递的year和month参数，转为int类型
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        # 按照year和month过滤文章
        article_list = Article.objects.filter(created_time__year=year, created_time__month=month)
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list
