from django.shortcuts import render


def index(request):
    context = {
        'title': "Bot for English",
        'name_logo': "Bot",
        'category1': "Для учеников",
        'action1': "Получение результатов тестов",
        'sub_action1': "А так же получение новых заданий, слов и тестов",
        'category2': "Для учителя",
        'action2': "Проверка Д/З",
        'sub_action2': "Раздача новых домашних заданий, проверка слов и тестов",
        'category3': "Для будуших студентов",
        'action3': "Ознакомиться с курсами и ценами",
        'sub_action3': "Пощупать бота и получить консультацию",
    }

    return render(request, "main/index.html", context)
