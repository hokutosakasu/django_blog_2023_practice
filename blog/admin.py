from django.contrib import admin
from .models import Category,Post
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

admin.site.register(Category)
# admin.site.register(Post,MarkdownxModelAdmin)
admin.site.register(Post)