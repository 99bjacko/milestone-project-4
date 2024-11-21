from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blog'),
    path('<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('edit/<int:post_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete/<int:post_id>/', views.delete_blog_post, name='delete_blog_post'),
]
