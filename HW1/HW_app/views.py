from django.shortcuts import render
# from django.http import HttpResponse
from .models import Category, Product, Review
from django.db.models import Q


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
    reviews_count = Review.objects.filter(product_id=id).count()
    review = Review.objects.filter(product_id=id).exclude(text='niger').order_by('-date')
    data = {
        'products': product,
        'reviews': reviews_count,
        'review': review
    }
    return render(request, 'product.html', context=data)


def categories_list(request):
    text = request.GET.get('search_text', '')
    category = Category.objects.filter(name__contains=text)
    return render(request, 'categories.html', context={
        'category': category
    })


def review_list(request):
    review = Review.objects.all().exclude(text='niger').order_by('date')
    data = {
           'review': review
        }
    return render(request, 'reviews.html', context=data)