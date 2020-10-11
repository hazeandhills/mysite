from django import forms
from .models import Post
from .models import HomePage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class HomeForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ('title',)