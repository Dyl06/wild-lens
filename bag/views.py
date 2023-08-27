from django.shortcuts import render, redirect, reverse, HttpResponse, \
    get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to return the items in a bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST['size']
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if size in bag[item_id].keys():
            bag[item_id][size] += quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to {bag[item_id][size]}'  # noqa
            )
        else:
            bag[item_id][size] = quantity
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag')
    else:
        bag[item_id] = {
            size: quantity
        }
        messages.success(
            request,
            f'Added size {size.upper()} {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        item_id = request.POST.get('item_id')
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


# def adjust_bag(request, item_id):
#     """Adjust the quantity of a product in the bag"""

#     quantity = int(request.POST.get('quantity'))
#     size = request.POST['size']
#     bag = request.session.get('bag', {})

#     if quantity > 0:
#         bag[item_id] = quantity
#     else:
#         bag.pop(item_id)

#     request.session['bag'] = bag
#     return redirect(reverse('view_bag'))


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST['size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to {bag[item_id][size]}')  # noqa
        else:
            del bag[item_id][size]
            if not bag[item_id]:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
