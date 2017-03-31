from django.contrib import admin

# Register your models here.

from maiagogo.models import Category, Page, Post, UserProfile

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Post)
admin.site.register(UserProfile)
