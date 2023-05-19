from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


# 一覧を簡単に作る
class Index(ListView):
    model = Post


# 詳細を簡単に作る
class Detail(DetailView):
    model = Post
