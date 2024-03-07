from icecream import ic

from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


def get_token(request):
    user = User.objects.get(username='user')
    ic(user)
    token, isEmpty = Token.objects.get_or_create(user=user)
    ic(token)
    context = {
        'title': "Bot for English",
        'name_logo': "Bot",
        'token': token.key,
        'user': user
    }

    return render(request, "get_token/get_token.html", context)