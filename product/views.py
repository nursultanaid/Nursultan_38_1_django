from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from product.models import Product, Category

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