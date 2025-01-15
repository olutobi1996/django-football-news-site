from .models import PostComment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']  # Only include fields you want in the form
