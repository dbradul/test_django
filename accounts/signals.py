from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from accounts.models import Profile


user_action = Signal()

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
