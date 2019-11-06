from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.published.all()
    return render(request,
                 'blog/index.html', {'posts': posts})

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request,
                  'blog/detail.html', {'post': post})
