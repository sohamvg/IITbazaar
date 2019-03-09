from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from market.models import Product
from django.dispatch import receiver
'''
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
'''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userProducts = models.ManyToManyField(Product, blank=True)
    #stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()