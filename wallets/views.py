from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import WalletForm
from .models import Wallet, Currency

def index(request):
    context = {
        'title': 'Dashboard',
    }

    return render(request, 'wallets/index.html', context)


def wallets(request):
    context = {
        'title': 'Wallets',
        'wallets': Wallet.get_by_user(request.user)
    }

    return render(request, 'wallets/wallets.html', context)


def wallet_create(request):
    if request.method == 'POST':
        form = WalletForm(request.POST)
        if form.is_valid():
            wallet = Wallet()
            wallet.name = request.POST['name']
            wallet.balance = request.POST['balance']
            wallet.currency = Currency.objects.get(pk=request.POST['currency'])
            wallet.is_active = 'is_active' in request.POST
            wallet.user = request.user
            wallet.save()

            return HttpResponseRedirect(reverse('wallets'))
    else:
        form = WalletForm()

    context = {
        'title': 'Create wallet',
        'form': form,
    }

    return render(request, 'wallets/wallet-create.html', context)