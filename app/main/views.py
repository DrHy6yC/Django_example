from django.shortcuts import render

from rest_framework import viewsets

from .serializers import (
    Quize,
    Constant,
    User, 
    UserQuize, 
    UserAnswer, 
    LevelUser, 
    AccesUser, 
    QuizeAnswer, 
    QuizeQuestion, 
    QuizeTrueAnswer, 
    StatusQuize,
    QuizeSerializer,
    ConstantSerializer,
    UserSerializer,
    UserQuizeSerializer
) 


class QuizeViewSet(viewsets.ModelViewSet):
    queryset = Quize.objects.all().order_by('quize_name')
    serializer_class = QuizeSerializer

class ConstantViewSet(viewsets.ModelViewSet):
    queryset = Constant.objects.all().order_by('constant_name')
    serializer_class = ConstantSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id_user_tg')
    serializer_class = UserSerializer


class UserQuizeViewSet(viewsets.ModelViewSet):
    queryset = UserQuize.objects.all().order_by('id')
    serializer_class = UserQuizeSerializer


def test(request):
    context = {
        'title': "Bot for English",
        'name_logo': "Bot"
    }

    return render(request, "main/test.html", context)

def index(request):
    context = {
        'title': "Bot for English",
        'name_logo': "Bot",
        'categories': [
            {
                'category_name': "Для учеников",
                'action': "Получение результатов тестов",
                'sub_action': "А так же получение новых заданий, слов и тестов",
                'item': 'item item-1'
            },
            {
                'category_name': "Для учителя",
                'action': "Проверка Д/З",
                'sub_action': "Раздача новых домашних заданий, проверка слов и тестов",
                'item': 'item item-2'
            },
            {
                'category_name': "Для будуших студентов",
                'action': "Ознакомиться с курсами и ценами",
                'sub_action': "Пощупать бота и получить консультацию",
                'item': 'item item-3'
            }
        ]
    }

    return render(request, "main/index.html", context)
