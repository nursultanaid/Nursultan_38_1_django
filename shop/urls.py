from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product.views import (main_view, hello_view, current_data_view, goodbye_view,product_list_view,
                           product_detail_view, category_view, product_create_view, review_view,
                           HelloView, CurrentDateView, GoodbyeView, MainView, ProductListView,
                           ProductDetailView, CategoryView, ProductCreateView, ReviewView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_view, name='main'),
    path('main2/', MainView.as_view(), name='main2'),

    path('current_data/', current_data_view, name='current_data'),
    path('current_data2/', CurrentDateView.as_view(), name='current_data2'),

    path('goodbye/', goodbye_view, name='goodbye'),
    path('goodbye2/', GoodbyeView.as_view(), name='goodbye2'),

    path('hello/', hello_view, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),

    path('products/', product_list_view, name='product_list'),
    path('products2/', ProductListView.as_view(), name='product_list2'),


    path('products/<int:product_id>', product_detail_view, name='product_detail'),
    path('products/<int:product_id>.2/', ProductDetailView.as_view(), name='product_detail2'),


    path('category/', category_view, name='category'),
    path('category2/', CategoryView.as_view(), name='category2'),


    path('product_create/', product_create_view, name='product_create'),
    path('product_create2/', ProductCreateView.as_view(), name='product_create2'),


    path('reviews/', review_view, name='reviews'),
    path('reviews2/', ReviewView.as_view(), name='reviews2')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
