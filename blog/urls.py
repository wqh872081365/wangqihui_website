from django.conf.urls import url
from . import views
from . import tests

# from django.contrib import admin

urlpatterns = [
    url(r'index/$', views.IndexView.as_view()),
    url(r'^test/', tests.test_add),
]
