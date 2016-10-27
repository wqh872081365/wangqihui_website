# -*- coding:utf-8 -*-

# from django.contrib.auth.models import User, Group
from blog.models import Article, Category, Tag
from rest_framework import viewsets
from serializers import ArticleSerializer, CategorySerializer, TagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request):
    return Response({
        'articles': reverse('article_list', request=request),
        'categorys': reverse('category_list', request=request),
        'tags': reverse('tag_list', request=request),
    })


class ArticleListView(APIView):

    def get(self, request):
        articles = Article.objects.filter(status='p').order_by('-last_modified_time')
        serializer = ArticleSerializer(articles, many=True, context={'request': request})
        # print serializer.data
        result = {
            "data": serializer.data,
            "count": articles.count(),
        }
        return Response(result)


class ArticleDetailView(APIView):

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        serializer = ArticleSerializer(article, context={'request': request})
        result = {
            "data": serializer.data,
        }
        return Response(result)


class CategoryListView(APIView):

    def get(self, request):
        categorys = Category.objects.all().order_by('-last_modified_time')
        serializer = CategorySerializer(categorys, many=True, context={'request': request})
        result = {
            "data": serializer.data,
            "count": categorys.count()
        }
        return Response(result)


class CategoryDetailView(APIView):

    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category, context={'request': request})
        result = {
            "data": serializer.data,
        }
        return Response(result)


class CategoryArticleListView(APIView):

    def get(self, request, category_id):
        articles = Article.objects.filter(category=category_id, status='p').order_by('-last_modified_time')
        serializer = ArticleSerializer(articles, many=True, context={'request': request})
        result = {
            "data": serializer.data,
            "count": articles.count()
        }
        return Response(result)


class TagListView(APIView):

    def get(self, request):
        tags = Tag.objects.all().order_by('-last_modified_time')
        serializer = TagSerializer(tags, many=True, context={'request': request})
        result = {
            "data": serializer.data,
            "count": tags.count()
        }
        return Response(result)


class TagDetailView(APIView):

    def get(self, request, tag_id):
        tag = Tag.objects.get(id=tag_id)
        serializer = TagSerializer(tag, context={'request': request})
        result = {
            "data": serializer.data,
        }
        return Response(result)


class TagArticleListView(APIView):

    def get(self, request, tag_id):
        tag = Tag.objects.get(id=tag_id)
        articles = tag.article_set.all().filter(status='p').order_by('-last_modified_time')
        serializer = ArticleSerializer(articles, many=True, context={'request': request})
        result = {
            "data": serializer.data,
            "count": articles.count()
        }
        return Response(result)

