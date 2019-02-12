from django.shortcuts import render


def index(request):
    context = {
        'title': 'Dashboard',
    }

    return render(request, 'wallets/index.html', context)


def wallets(request):
    context = {
        'title': 'Wallets',
        'wallets': [
            {
                'id': 1,
                'name': 'Sberbank Card',
                'is_active': True,
                'currency': 'RUB',
                'account_balance': 2500.40
            },
            {
                'id': 2,
                'name': 'Savings',
                'is_active': True,
                'currency': 'RUB',
                'account_balance': 435000
            },
            {
                'id': 3,
                'name': 'Salary Card',
                'is_active': False,
                'currency': 'RUB',
                'account_balance': 0
            },
            {
                'id': 4,
                'name': 'Sberbank deposit',
                'is_active': True,
                'currency': 'RUB',
                'account_balance': 200000
            }
        ]
    }

    return render(request, 'wallets/wallets.html', context)


def wallet_create(request):
    context = {
        'title': 'Create wallet',
        'currencies': [
            {
                'id': 1,
                'name': 'USD',
            },
            {
                'id': 2,
                'name': 'EUR',
            },
            {
                'id': 3,
                'name': 'RUB',
            },
        ]
    }

    return render(request, 'wallets/wallet-create.html', context)