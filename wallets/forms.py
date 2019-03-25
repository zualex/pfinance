from django import forms
from .models import Wallet, Transaction, Category


class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['name', 'currency', 'is_active', 'balance']


class TransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)

        try:
            if 'instance' in kwargs:
                type_transaction = kwargs['instance'].type_transaction
            else:
                type_transaction = kwargs['initial']['type_transaction']

            self.fields["category"].queryset = Category.objects.filter(type_transaction=type_transaction)
        except KeyError:
            pass

    class Meta:
        model = Transaction
        widgets = {
            'type_transaction': forms.RadioSelect()
        }
        fields = ['wallet', 'category', 'type_transaction', 'value']  # TODO добавить datetime