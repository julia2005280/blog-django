from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '_all_'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '_all_'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '_all_'

class SearchForm(forms.Form):
    title = forms.CharField(label='Buscar por título', max_length=100, required=False)