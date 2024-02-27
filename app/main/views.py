from django.shortcuts import render


def index(request):
    context = {
        'title': "Bot for English",
        'name_logo': "Bot",
        'content': "",
    }

    return render(request, "main/index.html", context)
