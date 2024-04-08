from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/', null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)
    rate = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)