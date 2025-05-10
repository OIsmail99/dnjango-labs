from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Comment, Author
posts = Post.objects.all()

# Create your views here.

def index(request):
    return render(request, 'posts/index.html', {'posts': posts})

def post(request, post_id):
    post = posts.filter(id=post_id).first()
    if post:
        return render(request, 'posts/post.html', {'post': post})
    else:
        return HttpResponse("Post not found.")

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    if author:
        return render(request, 'posts/author.html', {'author': author})
    else:
        return HttpResponse("Author not found.")