from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    readonly_fields = ('created_date', 'modified_date')
    ordering = ('-created_date',)
    # when click on email or username it will open detail page
    list_display_links = ('product_name', 'price', 'stock','category')

admin.site.register(Product, ProductAdmin)