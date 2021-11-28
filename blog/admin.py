from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Category, Post
#from myblog.blog import models

# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'descriptions', 'url', 'add_date']
    search_fields = ('id',)


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', ]
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = (
            "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js", 'js/script.js',)
