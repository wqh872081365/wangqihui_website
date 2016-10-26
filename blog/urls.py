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

    # url(r'api/', api_root),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'api/articles/$', rest_views.ArticleListView.as_view()),
    url(r'api/articles/(?P<article_id>\d+)/$', rest_views.ArticleDetailView.as_view()),
    url(r'api/categorys/$', rest_views.CategoryListView.as_view()),
    url(r'api/categorys/(?P<category_id>\d+)/$', rest_views.CategoryDetailView.as_view()),
    url(r'api/tags/$', rest_views.TagListView.as_view()),
    url(r'api/tags/(?P<tag_id>\d+)/$', rest_views.TagDetailView.as_view()),
)

# urlpatterns = format_suffix_patterns(urlpatterns)
