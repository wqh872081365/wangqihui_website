from django.conf.urls import url
from . import views
from . import tests

# from django.contrib import admin

urlpatterns = [
    url(r'index/$', views.IndexView.as_view(), name='blog_index'),
    url(r'test/', tests.test_add),
    url(r'article/(?P<article_id>\d+)/$', views.ArticleDetailView.as_view(), name='blog_article_detail'),
    url(r'category/(?P<category_id>\d+)/$', views.CategoryView.as_view(), name='blog_category'),
    url(r'tag/(?P<tag_id>\d+)/$', views.TagView.as_view(), name='blog_tag'),
    url(r'^archive/(?P<year>\d+)/(?P<month>\d+)/$', views.ArchiveView.as_view(), name='blog_archive'),
]
