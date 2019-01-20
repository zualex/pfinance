from django.test import TestCase

from django.contrib.auth.models import User
from .models import Wallet, Currency


class WalletModelTests(TestCase):
    # TODO auto load fixture
    fixtures = [
        '/code/pfinance/fixtures/currencies.json',
        '/code/pfinance/fixtures/type_transactions.json',
        '/code/pfinance/fixtures/categories.json',
    ]

    def setUp(self):
        currency = Currency.objects.get(name="RUB")

        self.user = User.objects.create_user(username='testuser', password='12345')
        self.wallet = Wallet.objects.create(
            user=self.user,
            currency=currency,
            name='testwallet',
            is_active=True
        )

    def test_get_total_amount_income(self):
        self.assertEqual(self.wallet.get_total_amount_income(), 100)