from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'sub_category', 'pan_india', 'created_at')
    search_fields = ('name', 'category', 'sub_category')
    list_filter = ('category', 'sub_category', 'pan_india', 'created_at')
    prepopulated_fields = {'slug': ('name',)}