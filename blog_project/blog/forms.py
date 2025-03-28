from django import forms
from .models import BlogPost  # Ensure BlogPost is correctly imported

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
