from django.shortcuts import render
from .models import *


def main_page(request):
    products = Product.objects.all()
    context = {
        'title': 'Main',
        'products': products,
    }
    return render(request, 'main/index_main.html', context)


def category_page(request, category):
    products = Product.objects.filter(category__name=category)
    context = {
        'title': 'Category',
        'products': products,
    }
    return render(request, 'main/index_category.html', context)


def product_info(request, category, p_slug):
    prod = Product.objects.get(slug=p_slug)
    comments = Comment.objects.filter(product__slug=prod.slug)
    context = {
        'title': 'Product',
        'prod': prod,
        'comments': comments,
    }

    if request.method == 'POST':
        Comment.objects.create(user_name=request.POST['user_name'],
                               comment=request.POST['comment'],
                               product=prod)
    return render(request, 'main/index_product_info.html', context)
