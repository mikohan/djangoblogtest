from django.contrib import admin

from elastic.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)
