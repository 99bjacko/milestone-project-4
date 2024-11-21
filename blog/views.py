from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm
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

@login_required
def add_blog_post(request):
    """ Add a blog post to the blog page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store administrators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = BlogPostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)