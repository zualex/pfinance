from django.forms import ModelForm
from .models import Wallet, Transaction

class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = ['name', 'currency', 'is_active', 'balance']



class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['wallet', 'category', 'type_transaction', 'value']  # TODO добавить datetime
