import datetime
import os
import uuid

from django.test import TransactionTestCase

from django.contrib.auth import get_user_model

from django.db import models, transaction, DatabaseError

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BankAccount(models.Model):
    """_summary_
    Each Registered User has a Bank Account
    default balance => 0.00
    auto generated account_number through phone number
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bank')

    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Account Balance"),
                                  default=0.00)

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

class AssociateBank(models.Model):
    """_summary_
    Associate Bank Models. Needed for Direct Deposits and Withdrawal

    pass for now. Need further Research
    """
    pass

# class CardVerification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=_('card'))

#     card_number = models.PositiveBigIntegerField(verbose_name=_("Card Number"),
#                                                  help_text=_("Enter 16 digit card number"))

#     cvv = models.PositiveIntegerField(verbose_name=_("Card Verification Value"))

class Deposit(models.Model):
    """_summary_
    The deposit models that handles deposits from personal Bank to Mobile Wallet
    """
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

    Withdrawal_to = models.ForeignKey(AssociateBank, on_delete=models.CASCADE, related_name=_("associate_bank"))
    status = models.CharField(max_length=10, verbose_name=_("Deposit Status"),
                              choices=DepositStatus, default=DepositStatus.pending)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Deposit")
        verbose_name_plural = _("Deposits")

    def __str__(self) -> str:
        return f'{self.bank.user.username}-{self.amount}'


class InappTransFer(models.Model):

    class InappStatus(models.TextChoices):
        pending = ('pending', 'pending')
        successful = ('successful', 'successful')
        failed = ('failed', 'failed')

    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True)

    account_number = models.ForeignKey(BankAccount, on_delete=models.CASCADE,
                                       related_name=_('transactions'))

    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Amount"))

    status = models.CharField(max_length=20, verbose_name=_("Transaction Status"),
                              choices=InappStatus, default=InappStatus.pending)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    def __str__(self) -> str:
        return f'{self.account_number.user.username} - {self.amount}'


class OtherBankTransfer(models.Model):
    class TransferStatus(models.TextChoices):
        failed = ('failed', 'failed')
        pending = ('pending', 'pending')
        processing = ('processing', 'processing')
        successful = ('successful', 'successful')


    account_number = models.ForeignKey(BankAccount, related_name=_('other_transfer'),
                                       on_delete=models.CASCADE)

    recipient_account_number = models.PositiveBigIntegerField(verbose_name=_("Receivers Account Number"),
                                                              )
    bank_name = models.CharField(max_length=100, verbose_name=_("Receivers Bank Name"),
                                 blank=True)

    status = models.CharField(max_length=20, verbose_name=_("Transaction Status"),
                              choices=TransferStatus, default=TransferStatus.pending)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Other Bank Transfer')
        verbose_name_plural = _('Other Bank Transfers')

    def __str__(self) -> str:
        return f'{self.account_number.account_number} to {self.recipient_account_number}'


class UtilityType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110)

    class Meta:
        verbose_name = _('Utility Type')
        verbose_name_plural = _('Utility Types')

    def __str__(self) -> str:
        return f'{self.account_number.account_number} to {self.recipient_account_number}'



class UtilityBillPayment(models.Model):
    bank = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name=_("withdrawal"))
    bill_type = models.ForeignKey(UtilityType, on_delete=models.CASCADE, related_name=_("utility_type"))