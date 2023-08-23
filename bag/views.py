from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def view_bag(request):
    """ A view to return the items in a bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    item_id = request.POST.get('item_id')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag.pop(item_id)

    request.session['bag'] = bag
    return HttpResponse(status=200)
