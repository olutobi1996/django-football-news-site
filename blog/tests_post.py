from django.test import TestCase, Client
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User

class CreatePostTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('create_post')  # Replace with your URL name


    def test_create_post_logged_in_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url, {
            'title': 'Test Post',
            'content': 'Test Content',
        })
        self.assertEqual(response.status_code, 302)  # Assuming a redirect on success
        self.assertTrue(Post.objects.filter(title='Test Post').exists())  # Verify post was created


class UpdatePostTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Original Title', content='Original Content', author=self.user)
        self.url = reverse('edit_post', args=[self.post.pk])  # Replace with your URL name

    def test_update_post_anonymous_user(self):
        response = self.client.post(self.url, {
            'title': 'Updated Title',
            'content': 'Updated Content',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login page
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Original Title')  # Verify no change

    def test_update_post_logged_in_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url, {
            'title': 'Updated Title',
            'content': 'Updated Content',
        })
        self.assertEqual(response.status_code, 302)  # Assuming a redirect on success
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')  # Verify update


class DeletePostTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.url = reverse('delete_post', args=[self.post.pk])  # Replace with your URL name

    def test_delete_post_logged_in_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)  # Assuming a redirect on success
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())  # Verify post was deleted