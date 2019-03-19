from django import forms
from .models import Wallet, Transaction


class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['name', 'currency', 'is_active', 'balance']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        widgets = {
            'type_transaction': forms.RadioSelect()
        }
        fields = ['wallet', 'category', 'type_transaction', 'value']  # TODO добавить datetime
