from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:post_id>/', views.post),
    # path('posts/', include('posts.urls')),
]