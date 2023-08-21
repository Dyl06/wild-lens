from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to return the items in a bag """

    return render(request, 'bag/bag.html')