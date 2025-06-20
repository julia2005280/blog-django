
from django.shortcuts import render, redirect
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm
from .models import Post

def home(request):
    return render(request, 'home.html')

def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add_author.html', {'form': form})

def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add_category.html', {'form': form})

def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add_post.html', {'form': form})

def search_posts(request):
    form = SearchForm(request.GET)
    posts = []
    if form.is_valid():
        title = form.cleaned_data['title']
        posts = Post.objects.filter(title__icontains=title)
    return render(request, 'search.html', {'form': form, 'posts': posts})
