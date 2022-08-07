import datetime
import os
import uuid

from django.test import TransactionTestCase

from django.contrib.auth import get_user_model

from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank')

    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Account Balance"))

    account_number = models.IntegerField(verbose_name=_("Account Number"), unique=True,
                                         blank=True, null=True)


    class Meta:
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self) -> str:
        return f'{self.user.username} - {self.account_number}'

    def save(self, *args, **kwargs):
        if not self.account_number:
            """
            Stores the Int version of Phonenumber as the account number
            07023456789 account number => 7023456789
            """
            self.account_number = int(self.user.phone_number[2:])
        return super().save(self, *args, **kwargs)


# class CardVerification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=_('card'))

#     card_number = models.PositiveBigIntegerField(verbose_name=_("Card Number"),
#                                                  help_text=_("Enter 16 digit card number"))

#     cvv = models.PositiveIntegerField(verbose_name=_("Card Verification Value"))

class Deposit(models.Model):
    class DepositStatus(models.TextChoices):
        failed = ('failed', 'failed')
        pending = ('pending', 'pending')
        processing = ('processing', 'processing')
        successful = ('successful', 'successful')

    bank = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name=_("deposit"))

    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=_("Amount"))
    status = models.CharField(max_length=10, verbose_name=_("Deposit Status"),
                              choices=DepositStatus, default=DepositStatus.pending)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Deposit")
        verbose_name_plural = _("Deposits")

    def __str__(self) -> str:
        return f'{self.bank.user.username}-{self.amount}'


class Withdrawal(models.Model):
    class DepositStatus(models.TextChoices):
        failed = ('failed', 'failed')
        pending = ('pending', 'pending')
        processing = ('processing', 'processing')
        successful = ('successful', 'successful')


    bank = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name=_("withdrawal"))

    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=_("Amount"))

    status = models.CharField(max_length=10, verbose_name=_("Deposit Status"),
                              choices=DepositStatus, default=DepositStatus.pending)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Deposit")
        verbose_name_plural = _("Deposits")

    def __str__(self) -> str:
        return f'{self.bank.user.username}-{self.amount}'


class InappTransaction(models.Model):

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


class BillType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=20)


class UtilityBillPayment(models.Model):
    bank = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name=_("withdrawal"))
    bill_type = models.ForeignKey(BillType, on_delete=models.CASCADE, related_name=_("bill_type"))