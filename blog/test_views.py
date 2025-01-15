from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post


class BlogPostListViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('blog_list')  # Replace 'blog_list' with your view's name
        Post.objects.create(title='First Post', content='Content of first post')

    def test_view_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'blog/blog_list.html')  # Replace with your template path

    def test_view_displays_posts(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'First Post')


class BlogPostDetailViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title='Test Post', content='Test Content')
        self.url = reverse('blog_detail', args=[self.post.pk])  # Adjust 'blog_detail' and args if necessary

    def test_view_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')  # Replace with your template path

    def test_view_displays_post_content(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'Test Content')

class RestrictedViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('restricted_view')  # Replace with the restricted view's name

    def test_redirect_for_anonymous_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Redirect to login page
        self.assertIn('/login/', response.url)

    def test_access_for_logged_in_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)