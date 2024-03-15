from django.contrib import admin
from django.urls import path

from product.views import hello_view, current_data_view, goodbye_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('current_data/', current_data_view),
    path('goodbye/', goodbye_view),
    path('hello/', hello_view),
]