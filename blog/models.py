from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = FroalaField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")

    class Meta:
        ordering = ('-created_on', 'author')
    def __str__(self):
        return f"{self.title} | written by {self.author}"


class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField(default=False)
    class Meta:
        ordering = ('-created_on', 'user')
    def __str__(self):
        return f"Comment{self.user.username} posted \"{self.comment}\" on {self.created_on}"

    def approve_comment(self):
        self.approve = True
        self.save()





