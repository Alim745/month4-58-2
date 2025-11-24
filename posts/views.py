from django.shortcuts import render, HttpResponse, redirect
from posts.models import Post
from posts.models import Post
from posts.forms import PostForm, PostForm2


def test_view(request):
    if request.method == 'GET':
        return HttpResponse('My first view')


def html_view(request):
    if request.method == 'GET':
        return render(request, 'base.html')


def posts_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/posts_list.html', {'posts': posts})


def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'posts/post_detail.html', {'post': post})
    

# def post_create_view(request):
#     if request.method == 'GET':
#         form = PostForm()
#         return render(request, 'posts/post_create.html', context={'form': form})
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if not form.is_valid():
#             return render(request, 'posts/post_create.html', context={'form': form})
#         image = form.cleaned_data.get('image')
#         title = form.cleaned_data.get('title')
#         content = form.cleaned_data.get('content')
#         rate = form.cleaned_data.get('rate')
#         try:
#             post = Post.objects.create(image=image, title=title, content=content, rate=rate)
#             return redirect("/posts")
#         except Exception as e:
#             return HttpResponse(f'Error: {e}')
        

def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        try:
            form.save()
            return redirect("/posts")
        except Exception as e:
            return HttpResponse(f'Error: {e}')