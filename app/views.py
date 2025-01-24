from django.shortcuts import render, redirect

from app.models import User, Post
from .forms import AuthorPostsForm


# Create your views here.

def main(request):
    return render(request, 'main.html')

def all_authors(request):
    authors = User.objects.filter().all()
    return render(request, 'posts/all_authors.html', {'authors': authors})

def all_posts_author(request):

    if request.method == 'GET':
        form = AuthorPostsForm()
        return render(request, 'posts/author_posts.html', {"form": form})

    elif request.method == 'POST':
        form = AuthorPostsForm(request.POST)
        posts = []
        if form.is_valid():
            author = form.cleaned_data['author']
            posts = Post.objects.filter(author=author)

        return render(request, 'posts/author_posts.html', {"form": form, "posts": posts})


def detail_post(request, id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return redirect("all_posts_author")

        return render(request, 'posts/detail_page.html', {'post': post})
