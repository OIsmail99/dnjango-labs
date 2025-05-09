from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
posts = [
    {
        'id': 1,
        'title': 'Post 1',
        'content': 'Content of post 1',
    },
    {
        'id': 2,
        'title': 'Post 2',
        'content': 'Content of post 2',
    },
    {
        'id': 3,
        'title': 'Post 3',
        'content': 'Content of post 3',
    },
    {
        'id': 4,
        'title': 'Post 4',
        'content': 'Content of post 4',
    },
    {
        'id': 5,
        'title': 'Post 5',
        'content': 'Content of post 5',
    },
]

def index(request):
    return HttpResponse('Hello, world! This is the index view of the posts app.')