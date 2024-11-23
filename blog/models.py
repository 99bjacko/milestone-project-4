from django.db import models


class BlogPost(models.Model):
    main_title = models.CharField(max_length=254)
    sub_title = models.CharField(max_length=254, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    post_content = models.TextField()

    def __str__(self):
        return self.main_title
