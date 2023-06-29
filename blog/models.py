from distutils.command.upload import upload
from django.db import models
from django.utils import timezone # django で日付を管理するためのモジュール
from markdownx.models import MarkdownxField
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify
from mdeditor.fields import MDTextField # 追加

# Create your models here.
class Category(models.Model):
    category=models.CharField('カテゴリー',max_length=200)

    def __str__(self):
        # return self.category
        return self.category


class Post(models.Model):
    title=models.CharField('タイトル',max_length=200)
    #text=models.TextField('本文')
    text = MDTextField() # 変更
    #text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')
    image=models.ImageField('画像',upload_to='images/Title/',blank=True)
    category=models.ForeignKey(Category,verbose_name='カテゴリー',on_delete=models.CASCADE)
    created_date=models.DateTimeField('日付',default=timezone.now) #ロンドン時間
    updated_data=models.DateTimeField('更新日時',auto_now=True)     #ロンドン時間
    
    # """ カスタムメソッド """
    def get_text_markdownx(self):
        return mark_safe(markdownify(self.text))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'


class PostView(models.Model):
    """記事ビューモデル"""

    class Meta:
        db_table = 'V_PostCategory'
        verbose_name = verbose_name_plural = '記事View'

    title=models.CharField('タイトル',max_length=200)
    text = MDTextField() # 変更
    image=models.ImageField('画像',upload_to='images/Title/',blank=True)
    created_date=models.DateTimeField('日付',default=timezone.now) #ロンドン時間
    updated_data=models.DateTimeField('更新日時',auto_now=True)     #ロンドン時間
    category=models.ForeignKey(Category,verbose_name='カテゴリー',on_delete=models.CASCADE)
    category=models.CharField('カテゴリー',max_length=200)

    def __str__(self):
        return self.title