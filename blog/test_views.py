from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, PostComment
from blog.forms import CommentForm
from django.utils.text import slugify


class BlogViewsTest(TestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.other_user = User.objects.create_user(username='otheruser', password='testpassword')

        # Create a published post
        self.post = Post.objects.create(
            title="Test Post",
            content="This is the content of the test post.",
            slug="test-post",
            status=1,  # Published
            author=self.user
        )

        # Create a draft post
        self.draft_post = Post.objects.create(
            title="Draft Post",
            content="This is a draft post.",
            slug="draft-post",
            status=0,  # Draft
            author=self.user
        )

        # Create a comment for the published post
        self.comment = PostComment.objects.create(
            comment="This is a test comment.",
            user=self.user,
            post=self.post
        )

    def test_post_list_view(self):
        """Test the PostList view."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

        # Ensure only published posts are displayed
        posts = response.context['post_list']
        self.assertIn(self.post, posts)
        self.assertNotIn(self.draft_post, posts)

    def test_post_detail_view(self):
        """Test the post_detail view for a published post."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

        # Ensure post details and comments are included
        self.assertEqual(response.context['post'], self.post)
        self.assertIn(self.comment, response.context['comments'])

    def test_post_detail_unauthenticated(self):
        """Test that unauthenticated users are redirected to login."""
    response = self.client.get(reverse('post_detail', args=[self.post.slug]))
    self.assertRedirects(response, f'/accounts/login/?next=/{self.post.slug}/')

    def test_comment_edit_view(self):
        """Test that the owner can edit their comment."""
        self.client.login(username='testuser', password='testpassword')
        url = reverse('comment_edit', args=[self.post.slug, self.comment.sno])

        data = {'comment': 'This is an edited comment.'}
        response = self.client.post(url, data)

        self.comment.refresh_from_db()
        self.assertEqual(self.comment.comment, 'This is an edited comment.')
        self.assertRedirects(response, reverse('post_detail', args=[self.post.slug]))

    def test_comment_edit_unauthorized(self):
        """Test that unauthorized users cannot edit comments."""
        self.client.login(username='otheruser', password='testpassword')
        url = reverse('comment_edit', args=[self.post.slug, self.comment.sno])

        data = {'comment': 'Trying to edit someone else’s comment.'}
        response = self.client.post(url, data)

        self.comment.refresh_from_db()
        self.assertEqual(self.comment.comment, 'This is a test comment.')  # Ensure it’s unchanged
        self.assertRedirects(response, reverse('post_detail', args=[self.post.slug]))

    def test_comment_delete_without_slug(self):
        """Test comment deletion without using a slug."""
        self.client.login(username='testuser', password='testpassword')
        url = reverse('comment_delete_without_slug', args=[self.comment.sno])

        response = self.client.post(url)
        self.assertRedirects(response, reverse('home'))

        # Check that the comment is deleted
        with self.assertRaises(PostComment.DoesNotExist):
            PostComment.objects.get(pk=self.comment.sno)

    def test_comment_delete_unauthorized(self):
        """Test that unauthorized users cannot delete comments."""
        self.client.login(username='otheruser', password='testpassword')
        url = reverse('comment_delete_without_slug', args=[self.comment.sno])

        response = self.client.post(url)
        self.assertRedirects(response, reverse('home'))

        # Check that the comment still exists
        self.assertTrue(PostComment.objects.filter(pk=self.comment.sno).exists())

    def test_post_search(self):
        """Test the search functionality."""
        url = reverse('post_search')
        query = {'q': 'Test'}
        response = self.client.get(url, query)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/search_results.html')

        # Ensure the correct results are returned
        results = response.context['results']
        self.assertIn(self.post, results)
        self.assertNotIn(self.draft_post, results)

    def test_post_search_no_query(self):
        """Test search with no query returns no results."""
        url = reverse('post_search')
        response = self.client.get(url, {'q': ''})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/search_results.html')

        results = response.context['results']
        self.assertEqual(len(results), 0)
