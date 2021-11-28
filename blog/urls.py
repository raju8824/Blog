from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name='home'),
    path("post/<slug:url>", views.post, name='post'),
    path("category/<slug:url>", views.category, name='category'),
]
