import datetime
import os
from tokenize import blank_re
from django.contrib.auth import get_user_model

from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _


User = get_user_model()


# class ImageUploadPath:
#     def __init__(self) -> None:
#         username = self.instance.user


def upload_to(instance, filename):
    username = instance.user
    today = datetime.today()
    return f"profile/{username}/{filename}.jpg"

def kyc_upload_front(instance, filename):
    username = instance.user
    return f'kyc/front/{username}/{filename}.jpg'

def kyc_upload_back(instance, filename):
    username = instance.user
    return f'kyc/back/{username}/{filename}.jpg'


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
    date_of_birth = models.DateField(blank=True, verbose_name="Date of Birth")
    account_number = models.IntegerField(verbose_name=_("Account Number"), unique=True,
                                         blank=True, null=True)
    residential_address = models.CharField(max_length=100, verbose_name=_("Residential Address"),
                                           blank=True)
    lga = models.models.CharField(max_length=100, verbose_name=_("Local Government Area"),
                                           blank=True)
    state = models.models.CharField(max_length=100, verbose_name=_("State"),
                                           blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = int(self.user.phone_number[2:])
        return super().save(*args, **kwargs)


class KycVerification(models.Model):
    class ValidIdOptions(models.TextChoices):
        nin = ('NIN', 'NIN')
        voters_card = ('Voters Card', 'Voters Card')
        passport = ("International Passport", 'International Passport')

    class KycLevelOptions(models.IntegerChoices):
        Level1 = (1, 'Level 1')
        Level2 = (2, 'Level 2')
        Level3 = (3, 'Level 3')

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name=_("kyc"))
    valid_id = models.CharField(max_length=20, verbose_name=_("Valid Identity Card"),
                                help_text=_("Select a Valid card you own from the options"),
                                choices=ValidIdOptions, blank=True)
    id_num = models.PositiveBigIntegerField(verbose_name=_("Id Unique Digits"),
                                            blank=True, null=True)
    front_image = models.ImageField(upload_to=kyc_upload_front, verbose_name=_("Id Front Image"),
                                    help_text=_("format -> jpg, Front Image of Id"), blank=True)
    back_image = models.ImageField(upload_to=kyc_upload_front, verbose_name=_("Id Back Image"),
                                    help_text=_("format -> jpg, Back Image of Id"), blank=True)
    upgraded_status = models.BooleanField(default=False,
                            help_text=_("True If all user's Information are valid and not null"),
                            verbose_name=_("Status Update"))
    kyc_level = models.IntegerField(verbose_name=_("Kyc Level Verification"),
                                 choices=KycLevelOptions, default=KycLevelOptions.1)

    def __str__(self) -> str:
        return f'{self.user.username}'

    class Meta:
        verbose_name = _("Kyc Information")
        verbose_name_plural = _("Kyc Information")
