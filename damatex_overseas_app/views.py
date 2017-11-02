from django.shortcuts import render, get_object_or_404
from .models import Category, Product, CarousalImages
from cart.forms import CartAddProductForm
from django.db.models import Q



# Create your views here.


def search(request):
    query = request.GET.get('q')
    carosual_images = CarousalImages.objects.all()
    if query:
        qs = Product.objects.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)
        )
    else:
        qs = None
    return render(request, 'shop/product/search.html', {'qs': qs, 'query': query, 'carosual_images': carosual_images})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    carosual_images = CarousalImages.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'carosual_images': carosual_images,
    }

    return render(request, 'shop/product/list.html',context)


def product_detail(request, id, slug):
    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    carosual_images = CarousalImages.objects.all()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'carosual_images': carosual_images,
    }
    return render(request, 'shop/product/detail.html', context)


# from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.conf import settings
import os


def Display(request, file_name):

    File_Name = file_name.replace('_', ' ')
    file_path = os.path.join(settings.MEDIA_ROOT, File_Name)

    with open(file_path,'r') as pdf:
        response = HttpResponse(pdf.read(), content_type = 'application/pdf')
        response['Content-Disposition'] = 'attachment;filename=%s' % File_Name
    return response

