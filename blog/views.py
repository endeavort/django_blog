from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


# 一覧
class Index(ListView):
    model = Post


# 個別
class Detail(DetailView):
    model = Post


# 新規作成
class Create(CreateView):
    model = Post

    # 編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]


# 編集
class Update(UpdateView):
    model = Post
    fields = ["title", "body", "category", "tags"]


# 削除
class Delete(DeleteView):
    model = Post

    # 削除したあとに移動する先（トップページ）
    success_url = "/"
