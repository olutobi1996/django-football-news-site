from django.db import models
from django.contrib.auth.models import User

content = models.TextField()
created_on = models.DateTimeField(auto_now_add=True)
STATUS = ((0, "Draft"), (1, "Published"))
status = models.IntegerField(choices=STATUS, default=0)
excerpt = models.TextField(blank=True)
updated_on = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)



class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)




