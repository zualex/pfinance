from django.urls import path

from . import views

app_name = 'wallets'
urlpatterns = [
    path('', views.index, name='index'),
    path('wallets', views.wallets, name='wallets'),
    path('wallets/create', views.wallet_create, name='wallet-create'),
    path('wallets/<int:wallet_id>/update', views.wallet_update, name='wallet-update'),
    path('wallets/<int:wallet_id>/delete', views.wallet_delete, name='wallet-delete'),

    path('transactions', views.transactions, name='transactions'),
    path('transactions/create', views.transaction_create, name='transaction-create'),
    path('transactions/<int:transaction_id>/update', views.transaction_update, name='transaction-update'),
    path('transactions/<int:transaction_id>/delete', views.transaction_delete, name='transaction-delete'),
]