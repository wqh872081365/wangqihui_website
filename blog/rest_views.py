# -*- coding:utf-8 -*-

# from django.contrib.auth.models import User, Group
from blog.models import Article, Category, Tag
from rest_framework import viewsets
from serializers import ArticleSerializer, CategorySerializer, TagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ArticleListView(APIView):

    def get(self, request):
        articles = Article.objects.filter(status='p').order_by('-last_modified_time')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetailView(APIView):

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class CategoryListView(APIView):

    def get(self, request):
        categorys = Category.objects.all().order_by('-last_modified_time')
        serializer = ArticleSerializer(categorys, many=True)
        return Response(serializer.data)


class CategoryDetailView(APIView):

    def get(self, request, category_id):
        articles = Article.objects.filter(category=category_id, status='p').order_by('-last_modified_time')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class TagListView(APIView):

    def get(self, request):
        tags = Tag.objects.all().order_by('-last_modified_time')
        serializer = ArticleSerializer(tags, many=True)
        return Response(serializer.data)


class TagDetailView(APIView):

    def get(self, request, tag_id):
        tag = Tag.objects.get(id=tag_id)
        articles = tag.article_set.all().filter(status='p').order_by('-last_modified_time')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


