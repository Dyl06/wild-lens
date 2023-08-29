from .models import Photographer


def get_photographer_list(request):

    GROUP_NAME_FOR_PHOTOGRAPHERS = "Photographers"
    
    user_is_photographer = request.user.groups.filter(name=GROUP_NAME_FOR_PHOTOGRAPHERS).exists()
    
    photographers = Photographer.objects.all()
    return {
        'get_photographer_list': photographers,
        'user_is_photographer': user_is_photographer
        }