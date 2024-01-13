import os
from django.db import models

def image_upload_path(instance, filename):
    return filename

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sweet', 'Sweets'),
        ('dhaba', 'Dhaba'),
    ]

    SUBCATEGORY_CHOICES = [
        ('khoya', 'Khoya'),
        ('bengoli', 'Bengoli'),
        ('laddu', 'Laddu'),
        ('chaat', 'Chaat'),
        ('snaks', 'Snaks'),
        ('kaju', 'Kaju'),
        ('chips', 'Chips'),
        ('mathi', 'Mathi'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/assets/img/product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=255, choices=SUBCATEGORY_CHOICES)
    pan_india = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name