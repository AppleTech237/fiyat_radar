from django.contrib import admin

# Register your models here.

from .models import Product, Price, Category

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at') 
    list_filter = ('category',) 

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'store', 'price', 'url_on_store', 'updated_at')
    list_filter = ('store', 'product')


