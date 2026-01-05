from django.shortcuts import render
from .models import Product

def store(request):
    products = Product.objects.all().filter(is_available=True)
    count = products.count()
    context = {"products": products, "count": count}
    return render(request, "store/store.html", context)