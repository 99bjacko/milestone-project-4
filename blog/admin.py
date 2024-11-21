from django.contrib import admin
from .models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'main_title',
        'sub_title',
        'post_content',
    )

admin.site.register(BlogPost, BlogPostAdmin)