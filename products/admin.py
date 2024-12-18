from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'selected')
    list_filter = ('selected',)
    search_fields = ('name', 'description')
    ordering = ('-id',)
