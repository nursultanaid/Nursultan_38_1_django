from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from product.models import Product

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
    print(products)
    for product in products:
        print(product)

    context = {'products': products}

    return render(request, 'product_list.html', context)
