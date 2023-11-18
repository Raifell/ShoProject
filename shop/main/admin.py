from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'count', 'date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'product', 'date')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
