import secrets

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from HW1 import settings
from .forms import ProductCreateForm, ReviewCreateForm, UserRegisterForm
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


def add_product(request):
    if request.method == 'GET':
        form = ProductCreateForm()
        data = {
            'form': form
        }
        return render(request, 'add_product.html', context=data)
    elif request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product/')
        else:
            return render(request, 'add_product.html',
                          context={'form': form})


@login_required(login_url='/login/')
def add_review(request):
    if request.method == 'GET':
        form = ReviewCreateForm
        data = {
            'form': form,
        }
        return render(request, 'add_review.html', context=data)
    elif request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review.objects.create(author=request.user, text=form.cleaned_data['text'],
                                  product=form.cleaned_data['product'])
            return redirect('/review/')
        else:
            return render(request, 'add_review.html',
                          context={'form': form})


from django.contrib import auth


def login(request):
    data = {}
    next = request.GET.get('next')
    if next:
        data = {
            'message': 'Авторизуйтесь для того, чтобы отсавить отзыв'
        }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            data['message'] = 'Неверный логин или пароль'
    return render(request, 'login.html', context=data)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST['email'],
                password=request.POST['password'],
                password1=request.POST['password1'],
                is_active=False
            )
            code = secrets.token_urlsafe(16)
            send_mail(
                subject='Activation code',
                message=f'http//:1270.0.1:8000/activate/{code}',
                from_email=settings.EMAIL_HOST,
                recipient_list=[request.POST['email']]
            )
        else:
            return render(request, 'register.html', context={
                'form': form
            })
    data = {
        'form': UserRegisterForm()
    }
    return render(request, 'register.html', context=data)
