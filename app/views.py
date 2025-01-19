from django.shortcuts import render

from app.models import User
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
        return render(request, 'posts/author_posts', {"form": form})

    elif request.method == 'POST':
        form = AuthorPostsForm(request.POST)
        if form.is_valid():
            user = form.save()
        return render(request, 'posts/author_posts', {"form": form})
