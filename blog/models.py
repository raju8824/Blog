from django.db import models
from django.utils.html import format_html


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px"/>'.format(self.image))


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    class Media:
        js = ('js/script.js',)

    def __str__(self):
        return self.title
