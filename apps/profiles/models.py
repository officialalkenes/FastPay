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
    class ValidIdOptions(models.TextChoices):
        nin = ('NIN', 'NIN')
        voters_card = ('Voters Card', 'Voters Card')
        passport = ("International Passport", 'International Passport')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    profile_pics = models.ImageField(upload_to=upload_to, verbose_name=_("Profile Picture"))
    gender = models.CharField(max_length=12, verbose_name=_("Gender"), choices=GenderOptions,
                              help_text=_('format: required, designates gender of user'))
    bvn_number = models.PositiveIntegerField(verbose_name=_("Bank Verification Number"),
                                             max_digits=11, min_digits=11,
                                             help_text=_("User's Bank Verification Number"),
                                             blank=True)
    date_of_birth = models.DateField(blank=True, verbose_name="Date of Birth")
    valid_id = models.CharField(max_length=20, verbose_name=_("Valid Identity Card"),
                                help_text=_("Select a Valid card you own from the options"),
                                choices=ValidIdOptions, blank=True)
    id_num = models.PositiveBigIntegerField(verbose_name=_("Id Unique Digits"),
                                            blank=True, null=True)
    account_number = models.IntegerField(verbose_name=_("Account Number"), unique=True,
                                         blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = ''
        return super().save(*args, **kwargs)