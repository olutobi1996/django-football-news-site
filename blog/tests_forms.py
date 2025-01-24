from django.test import TestCase
from blog.forms import CommentForm
from blog.models import Post, PostComment
from django.contrib.auth.models import User


class TestCommentForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(
            title="Test Post", 
            content="Test content", 
            slug="test-post", 
            status=1  # Published
        )

    def test_form_is_valid(self):
        data = {
            'content': 'This is a test comment',  # Assuming 'content' is a required field
            'post': self.post.id,  # Include the post ID or object
            'user': self.user.id,  # Include the user if needed
        }
        comment_form = CommentForm(data=data)
        self.assertTrue(comment_form.is_valid(), msg="Form Fail")
    
    def test_form_is_invalid(self):
        data = {
            'content': '',  # Invalid because content cannot be empty
        }
        comment_form = CommentForm(data=data)
        self.assertFalse(comment_form.is_valid())


class TestCommentForm(TestCase):
    def test_form_is_valid(self):
        data = {
            'content': 'This is a test comment',
        }
        comment_form = CommentForm(data=data)
        if not comment_form.is_valid():
            print(comment_form.errors)  # Print form errors for debugging
        self.assertTrue(comment_form.is_valid(), msg="Form Fail")

def test_form_is_valid(self):
    data = {
        'content': 'This is a valid comment',  # Only provide content if the view sets the other fields
    }
    comment_form = CommentForm(data=data)
    self.assertTrue(comment_form.is_valid(), msg="Form Fail")

comment = comment_form.save(commit=False)
comment.post = post
comment.user = request.user
comment.save()
