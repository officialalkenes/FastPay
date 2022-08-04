import datetime
import os
import uuid

from django.contrib.auth import get_user_model

from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank')
    account_number = models.PositiveBigIntegerField(verbose_name=_("Account Number"))
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Account Balance"))

    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self) -> str:
        return f'{self.user.username} - {self.account_number}'

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

    class TransactionStatus(models.TextChoices):
        pending = ('pending', 'pending')
        successful = ('successful', 'successful')
        failed = ('failed', 'failed')

    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True)
    account_number = models.ForeignKey(BankAccount, on_delete=models.CASCADE,
                                       related_name=_('transactions'))

    status = models.CharField(max_length=20, verbose_name=_("Transaction Status"),
                              choices=TransactionStatus, default=TransactionStatus.pending)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    def __str__(self) -> str:
        return f'{self.owner.username} - '

class Utility(models.Model):
    pass