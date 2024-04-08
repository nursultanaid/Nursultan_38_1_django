from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from product.forms import ProductForm, ProductForm2, ReviewForm
from product.models import Product, Category, Review


def hello_view(request):
    return HttpResponse("Hello! Its my project")

current_date = datetime.now()
def current_data_view(request):
    return HttpResponse(current_date)

def goodbye_view(request):
    return HttpResponse("Goodbye user!")

def main_view(request):
    context = {'name': 'Nursultan'}
    if request.method == "GET":
        return render(request, 'main.html', context=context)

def product_list_view(request):
    products = Product.objects.all()
    for product in products:
        print(product)

    context = {'products': products}

    return render(request, 'product/product_list.html', context)

def product_detail_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)

def category_view(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'product/category.html', context)

def product_create_view(request):
    if request.method == 'GET':
       form = ProductForm2()
       return render(request, 'product/product_create.html', {'form':form})

    if request.method == 'POST':
        form = ProductForm2(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'product/product_create.html', {'form':form})
        name = form.cleaned_data['name']
        title = form.cleaned_data['title']
        image = form.cleaned_data['image']
        price = form.cleaned_data['price']
        category = form.cleaned_data['category']
        tags = form.cleaned_data['tags']


        product = Product.objects.create(name=name, title=title, image=image, price=price, category=category)
        product.tags.set(tags)
        product.save()
        return redirect('/products/')

def review_view(request):
    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'product/review.html', {'form':form})

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if not form.is_valid():
            return render(request, 'product/review.html', {'form':form})
        text = form.cleaned_data['text']

        review = Review.objects.create(text=text)
        review.save()
        return redirect('/products/<int:product_id>/')