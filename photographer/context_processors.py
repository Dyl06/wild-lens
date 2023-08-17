from .models import Photographer


def get_photographer_list(request):
    photographers = Photographer.objects.all()
    # TODO: Sort alphabetically
    # TODO: Find only photographers with photos?
    print(photographers)
    return {'get_photographer_list': photographers}
