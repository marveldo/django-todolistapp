from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User



def createprofile(sender,created,instance,**kwargs):

    if created:
        user = instance
        Profile.objects.create(
            user = user,
            username = user.username,
            e_mail = user.email
        )


post_save.connect(createprofile, sender = User)
