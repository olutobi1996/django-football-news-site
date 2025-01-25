from django.test import TestCase
from blog.forms import CommentForm
from blog.models import Post, PostComment
from django.contrib.auth.models import User

from django.test import TestCase
from blog.models import PostComment, Post  # Adjust according to your actual model names
from django.contrib.auth.models import User
from blog.forms import CommentForm  # Assuming CommentForm is your form for comments

class TestCommentForm(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password")
        
        # Create a test post that the comment will be related to
        self.post = Post.objects.create(
            title="Test Post", 
            content="Test content", 
            slug="test-post", 
            status=1,  # Published
            author=self.user
        )

    def test_form_is_valid(self):
        """Test if the form is valid with proper data."""
        data = {
            'comment': 'This is a valid comment',  # This is the only field expected in your form
        }
        comment_form = CommentForm(data=data)

        # Debugging: Print form errors if the form is invalid
        if not comment_form.is_valid():
            print(comment_form.errors)  # Print form errors for debugging
        
        # Check if the form is valid
        self.assertTrue(comment_form.is_valid(), msg="Form should be valid with valid data.")

    def test_form_is_invalid(self):
        """Test if the form is invalid when required fields are missing."""
        data = {
            'comment': '',  # Invalid because 'comment' cannot be empty
        }
        comment_form = CommentForm(data=data)
        
        # Debugging: Print form errors if the form is invalid
        if not comment_form.is_valid():
            print(comment_form.errors)  # Print form errors for debugging
        
        # Check if the form is invalid
        self.assertFalse(comment_form.is_valid(), msg="Form should be invalid when comment is empty.")



