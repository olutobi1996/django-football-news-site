from django.test import TestCase
from .forms import CommentForm

class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'Well done!'})
        self.assertTrue(comment_form.is_valid(), msg="Form Fail")
    
    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form Pass")
