from django.shortcuts import render


def index(request):
    context = {
        'title': 'Example'
    }

    return render(request, 'wallets/index.html', context)