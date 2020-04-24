from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет, Мир!")

def test(request):
	return HttpResponse("Александра, ты любимка")