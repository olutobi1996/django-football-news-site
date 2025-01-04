from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    content=forms.Textarea()

    class Meta:
        model = Comment
        fields=['content']
