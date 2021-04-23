from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, JProfile, Coin, Item, Certificate, UserKey, Ranker

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_jprofile(sender, instance, created, **kwargs):
    if created:
        JProfile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_jprofile(sender, instance, **kwargs):
    instance.jprofile.save()


@receiver(post_save, sender=User)
def create_coin(sender, instance, created, **kwargs):
    if created:
        Coin.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_coin(sender, instance, **kwargs):
    instance.coin.save()


@receiver(post_save, sender=User)
def create_item(sender, instance, created, **kwargs):
    if created:
        Item.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_item(sender, instance, **kwargs):
    instance.item.save()


@receiver(post_save, sender=User)
def create_certificate(sender, instance, created, **kwargs):
    if created:
        Certificate.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_certificate(sender, instance, **kwargs):
    instance.certificate.save()


@receiver(post_save, sender=User)
def create_userkey(sender, instance, created, **kwargs):
    if created:
        UserKey.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_userkey(sender, instance, **kwargs):
    instance.userkey.save()


@receiver(post_save, sender=User)
def create_ranker(sender, instance, created, **kwargs):
    if created:
        Ranker.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_ranker(sender, instance, **kwargs):
    instance.ranker.save()
