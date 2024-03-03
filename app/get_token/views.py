from django.shortcuts import render

from rest_framework.authtoken.models import Token




def get_token(request):
    token = Token.objects.get_or_create(user='user')
    print(token.key)
    context = {
        'title': "Bot for English",
        'name_logo': "Bot",
        'token': "token.key"
    }

    return render(request, "main/test.html", context)