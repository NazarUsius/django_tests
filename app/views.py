from django.shortcuts import render

from app.models import User


# Create your views here.

def main(request):
    return render(request, 'main.html')

def all_authors(request):
    authors = User.objects.filter().all()
    return render(request, 'all_authors.html', {'authors': authors})
