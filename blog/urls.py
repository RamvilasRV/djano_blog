from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.bloglist, name="bloglist"),
    path("<int:pk>", views.BlogDetailView.as_view(), name="BlogDetailView"),
    path("<slug:username_slug>", views.UserBlogsView.as_view(), name='UserBlogsView')
]