from django.shortcuts import render, get_object_or_404

from .models import BlogPost
# Create your views here.

def all_blog_posts(request):
    """ A view to show all blog posts"""

    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)

def blog_post_detail(request, post_id):
    """ A view to show a specific blog post"""

    post = get_object_or_404(BlogPost, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_post_detail.html', context)