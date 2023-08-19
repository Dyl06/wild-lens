from .models import Photographer


def get_photographer_list(request):
    photographers = Photographer.objects.all()
    print(photographers)
    return {'get_photographer_list': photographers}