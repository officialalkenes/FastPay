from rest_framework import (serializers,
                            negotiation
                            )

from apps.banking.models import BankAccount


class UserBankAccountSerializer(serializers.ModelSerializer):
    username = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = BankAccount
        fields = '__all__'

    def save(self):
        user = serializers.CurrentUserDefault()  # <= magic!
        return super().save(self)


class AssociateBankSerializer(serializers.ModelSerializer):
    pass

