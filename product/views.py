from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import CreateView

from product.forms import ProductForm, ProductForm2, ReviewForm
from product.models import Product, Category, Review, Tag


class HelloView(View):
    def get(self,request):
        return HttpResponse("Hello! Its my project")

def hello_view(request):
    return HttpResponse("Hello! Its my project")

current_date = datetime.now()

class CurrentDateView(View):
    def get(self,request):
        return HttpResponse(current_date)

def current_data_view(request):
    return HttpResponse(current_date)

class GoodbyeView(View):
    def get(self,request):
        return HttpResponse("Goodbye user!")

def goodbye_view(request):
    return HttpResponse("Goodbye user!")

class MainView(View):
    def get(self,request):
        context = {'name': 'Nursultan'}
        return render(request, 'main.html', context=context)


def main_view(request):
    context = {'name': 'Nursultan'}
    if request.method == "GET":
        return render(request, 'main.html', context=context)

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        search = self.request.GET.get('search')
        sort = self.request.GET.get('sort', 'created_at')
        tag = self.request.GET.get('tag')
        page = self.request.GET.get('page', 1)

        posts = Product.objects.all()

        start = (int(page) - 1) * 3
        end = int(page) * 3

        if search:
            posts = posts.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )

        if tag:
            posts = posts.filter(tags__id=tag)

        return posts.order_by(sort)[start:end]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        posts = Product.objects.all()
        limit = 3

        all_pages = len(posts) / limit

        if round(all_pages) < all_pages:
            all_pages += 1
        all_pages = round(all_pages)

        context['all_pages'] = range(1, all_pages + 1)
        return context


def product_list_view(request):
    products = Product.objects.all()
    for product in products:
        print(product)

    context = {'products': products}

    return render(request, 'product/product_list.html', context)

class ProductDetailView(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)

        context = {'product': product}
        return render(request, 'product/product_detail.html', context)

def product_detail_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)

class CategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        context = {'category': category}
        return render(request, 'product/category.html', context)

def category_view(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'product/category.html', context)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm2
    template_name = 'products/products_create.html'
    success_url = '/products/'

    def get_absolute_url(self):
        if self.request.user.is_authenticated:
            return reverse('product_list')
        return reverse('login')


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

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'product/review.html', {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)

        if not form.is_valid():
            return render(request, 'product/review.html', {'form': form})
        text = form.cleaned_data['text']

        review = Review.objects.create(text=text)
        review.save()
        return redirect('/products/<int:product_id>/')


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