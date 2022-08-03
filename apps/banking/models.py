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
    account_number = models.PositiveBigIntegerField(verbose_name=_("Account Number"))

class CardVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=_('card'))

    card_number = models.PositiveBigIntegerField(verbose_name=_("Card Number"),
                                                 help_text=_("Enter 16 digit card number"))

    cvv = models.PositiveIntegerField(verbose_name=_("Card Verification Value"))

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deposit')
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, related_name=_("deposit-bank"))
    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=_("Amount"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Deposit")
        verbose_name_plural = _("Deposits")

    def __str__(self) -> str:
        return f'{self.user.username}-{self.amount}'


class Transaction(models.Model):
    pass

class Utility(models.Model):
    pass