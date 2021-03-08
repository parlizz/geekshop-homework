from django.shortcuts import render
import datetime
from mainapp.models import Product, ProductCategory


# Create your views here.

def index(request):
    dateTime = datetime.datetime.now()
    content = {
        'date': dateTime
    }
    return render(request, 'mainapp/index.html', content)


def products(request, id=None):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
