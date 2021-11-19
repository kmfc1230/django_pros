from django.contrib import admin

# Register your models here.
from .models import *


class BookManager(admin.ModelAdmin):
    # 列表页显示哪些字段的列
    list_display = ['id', 'title', 'pub', 'price', 'market_price', 'test']
    # 哪些字段可链接到修改 页
    list_display_links = ['title']
    # 添加过滤器
    list_filter = ['title', 'pub']
    # 添加搜索框
    search_fields = ['pub', 'title']
    # 在列表页可编辑字段
    list_editable = ['market_price']


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
    list_editable = ['age']
    search_fields = ['name']
    list_display_links = ['name']


admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
