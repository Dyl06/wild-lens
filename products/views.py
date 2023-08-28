from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, SubCategory, Photographer
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show the products page """

    products = Product.objects.all()
    query = ""
    categories = None
    subcategories = None
    photographers = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET.getlist('category')  # Use getlist to handle multiple selections
            if categories:
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)

        if 'photographer' in request.GET:
            photographers = request.GET.getlist('photographer')
            if photographers:
                products = products.filter(photographer__name__in=photographers)
                photographers = Photographer.objects.filter(name__in=photographers)

        if 'subcategory' in request.GET:
            subcategories = request.GET.getlist('subcategory')
            if subcategories:
                products = products.filter(subcategory__name__in=subcategories)
                subcategories = SubCategory.objects.filter(name__in=subcategories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                                request,
                                "Your search didn't match any items,"
                                "please try a different search criteria."
                               )
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query) |
                       Q(category__name__icontains=query) |
                       Q(subcategory__name__icontains=query))
            products = products.filter(queries).distinct()

            if not products.exists():
                messages.error(
                                request,
                                "Your search didn't match any items,"
                                "please try a different search criteria."
                               )
                return redirect(reverse('products'))

        queries = (Q(name__icontains=query) |
                   Q(description__icontains=query) |
                   Q(category__name__icontains=query) |
                   Q(subcategory__name__icontains=query))
        products = products.filter(queries).distinct()

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

    return render(request, 'products/product-page.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_page', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)