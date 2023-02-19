from django.db import models
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    '''
    カテゴリを作成する為のクラス
    '''
    name = models.CharField('カテゴリ', max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    '''
    投稿を作成する為のクラス
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)  # ユーザモデルが削除された時、投稿も削除される
    image = models.ImageField(
        upload_to='images', verbose_name='アップロード画像', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリ',
                                 on_delete=models.PROTECT)  # カテゴリーが削除された時、投稿が削除されないようにする

    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        """
        投稿フォームを作成する為の関数
        """
        return self.title
