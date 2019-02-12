from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wallets', views.wallets, name='wallets'),
    path('wallets/create', views.wallet_create, name='wallet-create'),
]