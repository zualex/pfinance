from django.conf import settings
from django.db import models


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