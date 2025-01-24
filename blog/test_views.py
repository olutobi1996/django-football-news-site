from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, PostComment
from blog.forms import CommentForm

class BlogViewsTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client = Client()

        # Create a sample post
        self.post = Post.objects.create(
            title="Test Post",
            content="Test content",
            slug="test-post",
            status=1,  # Published
        )

        # Create a sample comment
        self.comment = PostComment.objects.create(
            post=self.post,
            user=self.user,
            content="Test comment",
        )

    def test_post_list_view(self):
        response = self.client.get(reverse("post_list"))  # Replace "post_list" with your URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")
        self.assertContains(response, self.post.title)

    def test_post_detail_view_get(self):
        response = self.client.get(reverse("post_detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")
        self.assertContains(response, self.post.title)

    def test_post_detail_view_post_comment(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("post_detail", args=[self.post.slug]), {
            "content": "This is a new comment",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Comment added successfully!")
        self.assertEqual(self.post.comments.count(), 2)  # One existing + one new

    def test_comment_edit_view_get(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("comment_edit", args=[self.post.slug, self.comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/edit_comment.html")

    def test_comment_edit_view_post(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(
            reverse("comment_edit", args=[self.post.slug, self.comment.id]),
            {"content": "Updated comment"},
        )
        self.comment.refresh_from_db()
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(self.comment.content, "Updated comment")

    def test_comment_edit_view_permission_denied(self):
        other_user = User.objects.create_user(username="otheruser", password="password")
        self.client.login(username="otheruser", password="password")
        response = self.client.post(
            reverse("comment_edit", args=[self.post.slug, self.comment.id]),
            {"content": "Hacked comment!"},
        )
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertNotEqual(self.comment.content, "Hacked comment!")

    def test_comment_delete_view(self):
        self.client.login(username="testuser", password="password")
    response = self.client.post(reverse("comment_delete_without_slug", args=[self.comment.id]))
    self.assertEqual(response.status_code, 302)  # Expect redirection after deletion
    self.assertFalse(PostComment.objects.filter(id=self.comment.id).exists())  # Check deletion


    def test_comment_delete_view_permission_denied(self):
        other_user = User.objects.create_user(username="otheruser", password="password")
        self.client.login(username="otheruser", password="password")
        response = self.client.get(reverse("comment_delete_without_slug", args=[self.comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(PostComment.objects.filter(id=self.comment.id).exists())  # Not deleted

    def test_post_search_view(self):
        response = self.client.get(reverse("post_search") + "?q=test")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/search_results.html")
        self.assertContains(response, self.post.title)
