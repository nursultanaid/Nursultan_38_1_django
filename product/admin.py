# Register your models here.

from django.contrib import admin

from product.models import Product, Review, Tag, Category

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Category)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'title', 'rate', 'price', 'created_at', 'updated_at')
#     list_filter = ('created_at', 'updated_at')
#     search_fields = ('name', 'title')
#     readonly_fields = ('created_at', 'updated_at')
#
#     def save_model(self, request, obj, form, change):
#         obj.title = obj.title.capitalize()
#         super().save_model(request, obj, form, change)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(rate=0)

    # def has_add_permission(self, request):
    #     if Post.objects.count() >= 10:
    #         return False
    #     return True

    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
