from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    contents = forms.CharField(label="",widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Text goes here', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ['contents']
