from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import WalletForm, TransactionForm
from .models import Wallet, Currency, Transaction, Category, TypeTransaction


@login_required
def index(request):
    context = {
        'title': 'Dashboard',
    }

    return render(request, 'wallets/index.html', context)


@login_required
def wallets(request):
    context = {
        'title': 'Wallets',
        'wallets': Wallet.get_by_user(request.user)
    }

    return render(request, 'wallets/wallets.html', context)


@login_required
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

            return HttpResponseRedirect(reverse('wallets:wallets'))
    else:
        form = WalletForm()

    context = {
        'title': 'Create wallet',
        'form': form,
    }

    return render(request, 'wallets/wallet-create.html', context)


@login_required
def wallet_update(request, wallet_id):
    wallet = get_object_or_404(Wallet, pk=wallet_id)
    form = WalletForm(instance=wallet)

    if request.method == 'POST':
        wallet.name = request.POST['name']
        wallet.balance = request.POST['balance']
        wallet.currency = Currency.objects.get(pk=request.POST['currency'])
        wallet.is_active = 'is_active' in request.POST
        wallet.save()

        return HttpResponseRedirect(reverse('wallets:wallets'))

    context = {
        'title': 'Update wallet',
        'id': wallet_id,
        'form': form,
    }

    return render(request, 'wallets/wallet-update.html', context)


@login_required
def wallet_delete(request, wallet_id):
    if request.method == 'POST':
        wallet = get_object_or_404(Wallet, pk=wallet_id)
        wallet.delete()

    return HttpResponseRedirect(reverse('wallets:wallets'))


@login_required
def transactions(request):
    context = {
        'title': 'Transactions',
        'transactions': Transaction.get_by_user(request.user)
    }

    return render(request, 'transactions/transactions.html', context)


@login_required
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = Transaction()
            transaction.user = request.user
            transaction.wallet = Wallet.objects.get(pk=request.POST['wallet'])
            transaction.category = Category.objects.get(pk=request.POST['category'])
            transaction.type_transaction = TypeTransaction.objects.get(pk=request.POST['type_transaction'])
            transaction.value = request.POST['value']
            transaction.save()

            return HttpResponseRedirect(reverse('wallets:transactions'))
    else:
        form = TransactionForm()

    context = {
        'title': 'Create transaction',
        'form': form,
    }

    return render(request, 'transactions/transaction-create.html', context)


@login_required
def transaction_update(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    form = TransactionForm(instance=transaction)

    if request.method == 'POST':
        transaction.wallet = Wallet.objects.get(pk=request.POST['wallet'])
        transaction.category = Category.objects.get(pk=request.POST['category'])
        transaction.type_transaction = TypeTransaction.objects.get(pk=request.POST['type_transaction'])
        transaction.value = request.POST['value']
        transaction.save()

        return HttpResponseRedirect(reverse('wallets:transactions'))

    context = {
        'title': 'Update transaction',
        'id': transaction_id,
        'form': form,
    }

    return render(request, 'transactions/transaction-update.html', context)


@login_required
def transaction_delete(request, transaction_id):
    if request.method == 'POST':
        transaction = get_object_or_404(Transaction, pk=transaction_id)
        transaction.delete()

    return HttpResponseRedirect(reverse('wallets:transactions'))