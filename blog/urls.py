from django.conf.urls import url
from . import views
from . import tests

# from django.contrib import admin

urlpatterns = [
    url(r'index/$', views.IndexView.as_view(), name='index'),
    url(r'^test/', tests.test_add),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),
]
