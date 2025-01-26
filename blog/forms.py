from .models import PostComment
from django import forms

# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']  