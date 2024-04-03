from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product.views import (main_view, hello_view, current_data_view, goodbye_view,
                           product_list_view, product_detail_view, category_view)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_view, name='main'),
    path('current_data/', current_data_view, name='current_data'),
    path('goodbye/', goodbye_view, name='goodbye'),
    path('hello/', hello_view, name='hello'),
    path('products/', product_list_view, name='product_list'),
    path('products/<int:product_id>', product_detail_view, name='product_detail'),
    path('category/', category_view, name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
