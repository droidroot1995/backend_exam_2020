from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'author', 'content', 'added_at', 'for_class', 'subject']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'added_at']
