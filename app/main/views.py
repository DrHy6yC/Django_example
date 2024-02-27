from django.shortcuts import render


def index(request):
    # HttpResponse("Hello world")
    return render(request, "main/index.html")
