from django.shortcuts import render

from .models import BlogPost
# Create your views here.

def all_blog_posts(request):
    """ A view to show all blog posts"""

    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)