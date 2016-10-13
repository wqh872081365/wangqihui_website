from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'index/$', views.IndexView.as_view()),
]