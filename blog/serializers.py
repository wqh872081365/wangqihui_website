# from django.contrib.auth.models import User, Group
from blog.models import Article, Category, Tag
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "body", "status", "abstract", "views", "likes", "topped", "category", "created_time", "last_modified_time")


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', "created_time", "last_modified_time")


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', "created_time", "last_modified_time")
