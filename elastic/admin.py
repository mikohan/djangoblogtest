from django.contrib import admin

from elastic.models import Post, Category, CategoryPost, Product

admin.site.register(Post)
admin.site.register(Category)

admin.site.register(CategoryPost)

class ProductAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Product, ProductAdmin)
