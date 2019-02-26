from django.urls import path

from . import views

app_name = 'wallets'
urlpatterns = [
    path('', views.index, name='index'),
    path('wallets', views.wallets, name='wallets'),
    path('wallets/create', views.wallet_create, name='wallet-create'),
    path('wallets/<int:wallet_id>/update', views.wallet_update, name='wallet-update'),
]