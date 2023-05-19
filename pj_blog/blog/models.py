from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(  # 　文字の設定
        max_length=255,  # 最大の長さ
        blank=False,  # 入力必須（デフォルト）
        null=False,  # データベースの保存必須（デフォルト）
        unique=True,  # 一意の値（重複NG）
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    created = models.DateTimeField(  # 日時の設定
        auto_now_add=True,  # インスタンス作成時の日時を保存
        editable=False,  # 編集不可
        blank=False,
        null=False,
    )
    updated = models.DateTimeField(
        auto_now=True,  # 変更時に時間をアップデート
        editable=False,
        blank=False,
        null=False,
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    body = models.TextField(blank=True, null=False)  # 長さの制限がない文字の設定

    category = models.ForeignKey(  # 外部キーの設定
        Category, on_delete=models.CASCADE  # カテゴリーが削除されたら対応する行をす
    )

    tags = models.ManyToManyField(Tag, blank=True)  # 多対多の設定

    def __str__(self):
        return self.title
