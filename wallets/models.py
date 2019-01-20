from django.conf import settings
from django.db import models


class TypeTransaction(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_total_amount_income(self):
        return 100

    def get_total_amount_expense(self):
        return 50

    def get_total_amount(self):
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
    type_transaction = models.ForeignKey('TypeTransaction', on_delete=models.CASCADE)
    value = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    datetime = models.DateTimeField(auto_now_add=True)
