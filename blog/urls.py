from django.conf.urls import url, include, patterns
from . import views
from . import tests

# from django.contrib import admin

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import rest_views


urlpatterns = patterns(
    url(r'index/$', views.IndexView.as_view(), name='blog_index'),
    url(r'test/', tests.test_add),
    url(r'article/(?P<article_id>\d+)/$', views.ArticleDetailView.as_view(), name='blog_article_detail'),
    url(r'category/(?P<category_id>\d+)/$', views.CategoryView.as_view(), name='blog_category'),
    url(r'tag/(?P<tag_id>\d+)/$', views.TagView.as_view(), name='blog_tag'),
    url(r'archive/(?P<year>\d+)/(?P<month>\d+)/$', views.ArchiveView.as_view(), name='blog_archive'),

    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'api/$', rest_views.api_root),
    url(r'api/articles/list/$', rest_views.ArticleListView.as_view(), name='article_list'),
    url(r'api/articles/(?P<article_id>\d+)/$', rest_views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'api/categorys/list/$', rest_views.CategoryListView.as_view(), name='category_list'),
    url(r'api/categorys/(?P<category_id>\d+)/$', rest_views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'api/categorys/articles_list/(?P<category_id>\d+)/$', rest_views.CategoryArticleListView.as_view(), name='category_article_list'),
    url(r'api/tags/list/$', rest_views.TagListView.as_view(), name='tag_list'),
    url(r'api/tags/(?P<tag_id>\d+)/$', rest_views.TagDetailView.as_view(), name='tag_detail'),
    url(r'api/tags/articles_list/(?P<tag_id>\d+)/$', rest_views.TagArticleListView.as_view(), name='tag_article_list'),
)

# urlpatterns = format_suffix_patterns(urlpatterns)
