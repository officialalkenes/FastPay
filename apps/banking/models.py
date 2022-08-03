import datetime
import os

from django.contrib.auth import get_user_model

from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank')

    primary_bank = models.CharField(max_length=30, verbose_name=_("Primary Bank Name"))




class Deposit(models.Model):
    pass