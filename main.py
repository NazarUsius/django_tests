import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject.settings")
django.setup()
from app.models import User, Post

while True:
    ans = input("What operation would you like to perform? ")

    if ans == "create user":
        name = input("What is your name? ")
        last_name = input("What is your last_name? ")
        email = input("What is your email address? ")
        age = input("How old are you? ")
        User.objects.create(name=name, email=email, last_name=last_name, age=age)
        print("Successfully created user")

    if ans == "create post":
        author_name = input("What is the name of the post author? ")

        author = User.objects.filter(name=author_name).first()
        title = input("What is the title of the post? ")
        body = input("What is the body of the post? ")
        Post.objects.create(author=author, title=title, body=body)
        print("Successfully created post")

    if ans == "delete user":
        author_name = input("What is the name of the user you want to delete? ")

        user = User.objects.filter(name=author_name).first()
        user.delete()
        print("Successfully deleted user")











