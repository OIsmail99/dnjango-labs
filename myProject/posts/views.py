from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
posts = [
    {
        'id': 1,
        'title': 'Post 1',
        'content': 'Content of post 1',
        'image': 'posts/monkey.jpg',
    },
    {
        'id': 2,
        'title': 'Post 2',
        'content': 'Content of post 2',
        'image': '../media/monkey.jpg',
    },
    {
        'id': 3,
        'title': 'Post 3',
        'content': 'Content of post 3',
        'image': '../media/monkey.jpg',
    },
    {
        'id': 4,
        'title': 'Post 4',
        'content': 'Content of post 4',
        'image': '../media/monkey.jpg',
    },
    {
        'id': 5,
        'title': 'Post 5',
        'content': 'Content of post 5',
        'image': '../media/monkey.jpg',
    },
]

def index(request):
    return render(request, 'posts/index.html', {'posts': posts})

def post(request, post_id):
    post = {}
    for p in posts:
        if p['id'] == post_id:
            post = p
            break
    if post:
        return render(request, 'posts/post.html', {'post': post})
    else:
        return HttpResponse("Post not found.")