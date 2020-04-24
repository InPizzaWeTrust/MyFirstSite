from django.shortcuts import render


def delivery(request):
    return render(request, 'dostavka/delivery.html')