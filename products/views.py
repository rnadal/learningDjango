from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from .forms import RawProductForm

# Create your views here.

def product_create_view(request):
    my_form = ProductForm(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = ProductForm()

    # my_form = RawProductForm()
    # if request.method == 'POST':
    #     my_form = RawProductForm(request.POST)
    #     if my_form.is_valid():
    #         Product.objects.create(**my_form.cleaned_data)
    #     else:
    #         print(my_form.errors)

    context = {
        'form': my_form
    }
    return render(request, "product/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=3)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)