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
        self.income = TypeTransaction.get_income()
        self.expense = TypeTransaction.get_expense()

        self.user = User.objects.create_user(username='testuser', password='12345')
        self.wallet = Wallet.objects.create(
            user=self.user,
            currency=self.currency,
            name='testwallet',
            is_active=True
        )

    def test_get_total_amount_zero(self):
        self.assertEqual(self.wallet.get_total_amount_income(), 0)
        self.assertEqual(self.wallet.get_total_amount_expense(), 0)
        self.assertEqual(self.wallet.get_total_amount(), 0)

    def test_get_total_amount(self):
        category_income = Category.objects.filter(type_transaction=self.income)[0]
        category_expense = Category.objects.filter(type_transaction=self.expense)[0]

        values_income = [random.randrange(1, 10000, 1) for _ in range(5)]
        result_income = sum(values_income)

        values_expense = [random.randrange(1, 10000, 1) for _ in range(5)]
        result_expense = sum(values_expense)

        for value in values_income:
            Transaction.objects.create(
                user=self.user,
                wallet=self.wallet,
                category=category_income,
                type_transaction=self.income,
                value=value
            )

        for value in values_expense:
            Transaction.objects.create(
                user=self.user,
                wallet=self.wallet,
                category=category_expense,
                type_transaction=self.expense,
                value=value
            )

        self.assertEqual(self.wallet.get_total_amount_income(), result_income)
        self.assertEqual(self.wallet.get_total_amount_expense(), result_expense)
        self.assertEqual(self.wallet.get_total_amount(), result_income - result_expense)