from django.contrib import admin
from .models import User, Post
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')