from django.conf import settings
from django.db import models


class TypeTransaction(models.Model):
    DEFAULT_PK = 1
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    # TODO add cache
    @staticmethod
    def get_income():
        """Get income TypeTransaction."""
        return TypeTransaction.objects.get(name="income")

    # TODO add cache
    @staticmethod
    def get_expense():
        """Get expense TypeTransaction."""
        return TypeTransaction.objects.get(name="expense")


class Currency(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=False)
    balance = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_by_user(user):
        """Get wallets by user

        Args:
            user: object settings.AUTH_USER_MODEL

        Returns:
            QuerySet of wallets

        """
        return Wallet.objects.filter(user=user)

    def get_total_amount_income(self):
        """Get total amount income in wallet."""
        return Transaction.get_amount_by_wallet(self, TypeTransaction.get_income())

    def get_total_amount_expense(self):
        """Get total amount expense in wallet."""
        return Transaction.get_amount_by_wallet(self, TypeTransaction.get_expense())

    def get_total_amount(self):
        """Get total amount in wallet."""
        result = self.get_total_amount_income() - self.get_total_amount_expense()

        return result

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    type_transaction = models.ForeignKey('TypeTransaction', on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    type_transaction = models.ForeignKey(
        'TypeTransaction',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=TypeTransaction.DEFAULT_PK
    )
    value = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    datetime = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_amount_by_wallet(wallet, type_transaction):
        """Get amount by wallet and type transaciton

        Args:
            wallet: object Wallet
            type_transaction: object TypeTransaction

        Returns:
            Total amount

        """
        transactions = Transaction.objects.filter(
            wallet=wallet,
            user=wallet.user,
            type_transaction=type_transaction
        )

        result = sum([row.value for row in transactions])

        return result

    @staticmethod
    def get_by_user(user):
        """Get transactions by user

        Args:
            user: object settings.AUTH_USER_MODEL

        Returns:
            QuerySet of transactions

        """
        return Transaction.objects.filter(user=user)
