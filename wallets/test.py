from django.test import TestCase
from django.contrib.auth.models import User
from .models import Wallet, Currency, TypeTransaction, Category, Transaction
import random



class WalletModelTests(TestCase):
    # TODO auto load fixture
    fixtures = [
        '/code/pfinance/fixtures/currencies.json',
        '/code/pfinance/fixtures/type_transactions.json',
        '/code/pfinance/fixtures/categories.json',
    ]

    def setUp(self):
        self.currency = Currency.objects.get(name="RUB")
        self.income = TypeTransaction.objects.get(name="income")
        self.expense = TypeTransaction.objects.get(name="expense")

        self.user = User.objects.create_user(username='testuser', password='12345')
        self.wallet = Wallet.objects.create(
            user=self.user,
            currency=self.currency,
            name='testwallet',
            is_active=True
        )

    def test_get_total_amount_income(self):
        category = Category.objects.filter(type_transaction=self.income)[0]

        values = [random.randrange(1, 10000, 1) for _ in range(5)]
        result = sum(values)

        for value in values:
            Transaction.objects.create(
                user=self.user,
                wallet=self.wallet,
                category=category,
                type_transaction=self.income,
                value=value
            )

        self.assertEqual(self.wallet.get_total_amount_income(), 100)