from django.contrib import admin

from products.models import Basket, Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'stripe_product_price_id', 'category')
    readonly_fields = ['description', 'name']
    search_fields = ['name']
    ordering = ['-name']


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity']
    extra = 0
