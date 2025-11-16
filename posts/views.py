from django.shortcuts import render, HttpResponse
from posts.models import Post

def test_view(request):
    return HttpResponse('My first view')


def html_view(request):
    return render(request, 'base.html')


def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})
