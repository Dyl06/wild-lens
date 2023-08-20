from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, SubCategory, Photographer

# Create your views here.


def all_products(request):
    """ A view to show the products page """

    products = Product.objects.all()
    query = None
    categories = None
    subcategories = None
    photographers = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            print(categories)
            products = products.filter(category__name__in=categories)
            print(products)
            categories = Category.objects.filter(name__in=categories)
            print(categories)

        if 'photographer' in request.GET:
            photographers = request.GET['photographer'].split(',')
            print(photographers)
            products = products.filter(photographer__name__in=photographers)
            print(products)
            photographers = Photographer.objects.filter(name__in=photographers)
            print(photographers)

        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory'].split(',')
            products = products.filter(subcategory__name__in=subcategories)
            print(products)
            subcategories = SubCategory.objects.filter(name__in=subcategories)
            print(subcategories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Your search didn't match any items, please try a different search criteria.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query) | Q(subcategory__name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search': query,
        'categories': categories,
        'subcategories': subcategories,
        'photographers': photographers,
    }

    return render(request, 'products/products.html', context)


def product_page(request, product_id):
    """ A view to show the individual products on a page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_page.html', context)
