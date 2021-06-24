from django.shortcuts import render
# from django.http import HttpResponse
from .models import Category, Product, Review


# Create your views here.


def index(request):
    product = Product.objects.all()
    data = {
        'title': 'Товары',
        'products': product
    }
    return render(request, 'index.html', context=data)


def product_item(request, id):
    product = Product.objects.get(id=id)
    review = Review.objects.filter(product_id=id)
    data = {
        'products': product,
        'reviews': review
    }
    return render(request, 'product.html', context=data)


def categories_list(request):
    text = request.GET.get('search_text', '')
    category = Category.objects.filter(name__contains=text)
    return render(request, 'categories.html', context={
        'category': category
    })

