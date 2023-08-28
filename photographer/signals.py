from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Photographer

# Create the special access permission
content_type = ContentType.objects.get_for_model(Photographer)
permission, created = Permission.objects.get_or_create(
    codename='special_access',
    name='Special Access Permission',
    content_type=content_type,
)


# Assign the permission to users when a new Photographer is created
@receiver(post_save, sender=Photographer)
def assign_special_access(sender, instance, created, **kwargs):
    if created:
        instance.user.user_permissions.add(permission)
