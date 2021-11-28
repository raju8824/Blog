from django.shortcuts import render
from .models import Post, Category

# Create your views here.


def index(request):
    post = Post.objects.all()
    category = Category.objects.all()
    print(post)
    return render(request, 'myblog/home.html', {'post': post, 'billi': category})


def post(request, url):
    post = Post.objects.get(url=url)
    category = Category.objects.all()
    print(post)
    return render(request, 'myblog/post.html', {'post': post, 'cet': category})


def category(request, url):
    cat = Category.objects.get(url=url)
    post = Post.objects.filter(cat=cat)
    return render(request, 'myblog/category.html', {'cat': cat, 'post': post})
