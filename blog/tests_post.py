from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from blog.models import Post, PostComment
from blog.forms import CommentForm

class CommentEditViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a post
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            slug="test-post",
            status=1  # Published
        )

        # Create a comment for that post by the user
        self.comment = PostComment.objects.create(
            content="This is a test comment.",
            user=self.user,
            post=self.post
        )

        # Create another user for testing unauthorized access
        self.other_user = User.objects.create_user(username='otheruser', password='testpassword')

    def test_comment_edit_success(self):
        """Test that the owner can edit their comment successfully."""
        self.client.login(username='testuser', password='testpassword')

        # Define the URL for editing the comment
        url = reverse('comment_edit', args=[self.post.slug, self.comment.id])

        # Data for updating the comment
        data = {'content': 'This is the updated test comment.'}

        response = self.client.post(url, data)

        # Check if the comment was updated
        self.comment.refresh_from_db()

        # Assert the comment content was updated
        self.assertEqual(self.comment.content, 'This is the updated test comment.')

        # Check if it redirects to the post detail page
        self.assertRedirects(response, reverse('post_detail', args=[self.post.slug]))

        # Check for success message
        self.assertContains(response, 'Comment updated successfully!')

    def test_comment_edit_unauthorized(self):
        """Test that a user cannot edit someone else's comment."""
        self.client.login(username='otheruser', password='testpassword')

        # Define the URL for editing the comment
        url = reverse('comment_edit', args=[self.post.slug, self.comment.id])

        response = self.client.post(url)

        # Check that the comment content is unchanged
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'This is a test comment.')

        # Check if it redirects to the post detail page with an error message
        self.assertRedirects(response, reverse('post_detail', args=[self.post.slug]))
        self.assertContains(response, 'You are not authorized to edit this comment.')

    def test_comment_edit_invalid_form(self):
        """Test that when an invalid form is submitted, the comment is not updated."""
        self.client.login(username='testuser', password='testpassword')

        # Define the URL for editing the comment
        url = reverse('comment_edit', args=[self.post.slug, self.comment.id])

        # Submit an empty content to make the form invalid
        data = {'content': ''}

        response = self.client.post(url, data)

        # Check that the comment content is unchanged
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'This is a test comment.')

        # Check that the form is re-rendered with error messages
        self.assertFormError(response, 'form', 'content', 'This field is required.')

    def test_comment_edit_without_login(self):
        """Test that an unauthenticated user cannot access the edit page."""
        url = reverse('comment_edit', args=[self.post.slug, self.comment.id])

        response = self.client.get(url)

        # Check for redirect to login page
        self.assertRedirects(response, f'/accounts/login/?next={url}')
