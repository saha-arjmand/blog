from django.shortcuts import render
from account.models import Account

def home_view(request):

    context = {}

    accounts = Account.objects.all()

    context['accounts'] = accounts

    # return render(request, "account/account.html", context)

    return render(request, "home/home.html", context)