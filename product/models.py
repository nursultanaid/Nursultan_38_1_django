from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/', null=True, blank=True)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"
