import datetime
import os
from django.contrib.auth import get_user_model

from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _


User = get_user_model()

def upload_to(instance, filename):
    username = instance.user
    today = datetime.today()
    return f"profile/{username}/filename.jpg"

class Profile(models.Model):
    class GenderOptions(models.TextChoices):
        male = ('Male', 'Male')
        female = ('female', 'female')
        unspecified = ('Unspecified', 'Unspecified')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    profile_pics = models.ImageField(upload_to=upload_to, verbose_name=_("Profile Picture"))
    gender = models.CharField(max_length=12, verbose_name=_("Gender"), choices=GenderOptions,
                              help_text=_('format: required, designates gender of user'))
    bvn_number = models.PositiveIntegerField(verbose_name=_("Bank Verification Number"),
                                             max_digits=11, min_digits=11,
                                             help_text=_("User's Bank Verification Number"),
                                             blank=True)
    