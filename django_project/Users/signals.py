from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,UserMetaData,UserTotalHour

@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        UserMetaData.objects.create(user=instance)
        UserTotalHour.objects.create(user=instance)
        print("Request finished!")

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kawargs):
    instance.profile.save()