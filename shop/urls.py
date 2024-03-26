from django.contrib import admin
from django.urls import path

from product.views import main_view, hello_view, current_data_view, goodbye_view, product_list_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_view, name='main'),
    path('current_data/', current_data_view, name='current_data'),
    path('goodbye/', goodbye_view, name='goodbye'),
    path('hello/', hello_view, name='hello'),
    path('products/', product_list_view, name='product_list'),
]
