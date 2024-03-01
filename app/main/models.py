from django.db import models


class Constant(models.Model):
    constant_name = models.CharField(max_length=200, unique=True, blank=True, verbose_name="Наименование переменной")
    constant_value = models.CharField(max_length=200, blank=True, verbose_name="Значение переменной")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "constant"
        verbose_name = "Константа"
        verbose_name_plural = "Константы"

    def __str__(self) -> str:
        return self.constant_name


class LevelUser(models.Model):
    level_text = models.CharField(max_length=200, unique=True, blank=True, verbose_name="Уровень")
    min_level_score = models.IntegerField(blank=True, unique=True, verbose_name="Минималтный процент уровня")
    max_level_score = models.IntegerField(blank=True, unique=True, verbose_name="Максимальный процент уровня")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "level_user"
        verbose_name = "Уровень пользователя"
        verbose_name_plural = "Уровни пользователя"


class AccesUser(models.Model):
    acces_text = models.CharField(
        max_length=200, unique=True, blank=True, verbose_name="Название доступа"
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "acces_user"
        verbose_name = "Доступ"
        verbose_name_plural = "Доступы"


class StatusQuize(models.Model):
    status_text = models.CharField(max_length=200, unique=True, blank=True, verbose_name="Статус")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "status_quize"
        verbose_name = "Статус теста"
        verbose_name_plural = "Статусы теста"

    def __str__(self) -> str:
        return self.status_text


class Quize(models.Model):
    quize_name = models.CharField(max_length=200, unique=True, blank=True, verbose_name="Имя теста")
    quize_description = models.CharField(max_length=200, blank=True, verbose_name="Описание теста")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "quize"
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self) -> str:
        return self.quize_name


class QuizeAnswer(models.Model):
    id_quize = models.OneToOneField(
        Quize, models.CASCADE, blank=True, verbose_name="ID теста"
    )
    question_number = models.IntegerField(blank=True, verbose_name="Номер вопроса")
    answer_number = models.IntegerField(blank=True, verbose_name="Номер ответа")
    answer_text = models.CharField(max_length=200, blank=True, verbose_name="Текст ответа")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "quize_answer"
        verbose_name = "Ответ теста"
        verbose_name_plural = "Ответы теста"


class QuizeQuestion(models.Model):
    id_quize = models.OneToOneField(
        Quize, models.CASCADE, blank=True, verbose_name="ID теста"
    )
    question_number = models.IntegerField(blank=True, verbose_name="Номер вопроса")
    question_text = models.CharField(max_length=200, blank=True, verbose_name="Текст вопроса")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "quize_question"
        verbose_name = "Вопрос теста"
        verbose_name_plural = "Вопросы теста"


class QuizeTrueAnswer(models.Model):
    id_quize = models.OneToOneField(
        Quize, models.CASCADE, blank=True, verbose_name="ID теста"
    )
    id_answer = models.OneToOneField(
        QuizeAnswer, models.CASCADE, blank=True, verbose_name="ID ответа"
    )
    question_number = models.IntegerField(blank=True, verbose_name="Номер вопроса")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "quize_true_answer"
        verbose_name = "Правильный вопрос для теста"
        verbose_name_plural = "Правильные вопросы для теста"


class User(models.Model):
    id_user_tg = models.BigIntegerField(unique=True, blank=True, verbose_name="ID пользователя в телеграм")
    user_login = models.CharField(max_length=200, unique=True, blank=True, verbose_name="Лонин пользователя в телеграмм")
    user_full_name = models.CharField(max_length=200, blank=True, verbose_name="Полное имя и фамилия из телеграмм")
    user_level = models.OneToOneField(LevelUser, models.CASCADE, verbose_name='Уровень пользователя')
    user_access = models.OneToOneField(AccesUser, models.CASCADE, verbose_name='Доступ пользователя')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь в telegram"
        verbose_name_plural = "Пользователи в telegram"

    def __str__(self) -> str:
        return f"{self.id_user_tg} {self.user_login}"


class UserQuize(models.Model):
    id_user_tg = models.OneToOneField(
        User, models.CASCADE, to_field="id_user_tg", verbose_name='ID пользователя в телеграмм'
    )
    id_quize = models.OneToOneField(Quize, models.CASCADE, verbose_name='ID теста')
    quize_status = models.OneToOneField(StatusQuize, models.CASCADE, verbose_name='ID статуса теста')
    question_number = models.IntegerField(blank=True, verbose_name="Номер вопроса")
    id_answer_last = models.IntegerField(blank=True, verbose_name="ID последнего ответа пользователя")
    quize_score = models.IntegerField(verbose_name='Количество баллов пользователя')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "user_quize"
        verbose_name = "Запущенный тест пользователя"
        verbose_name_plural = "Запущенные тесты пользователя"


class UserAnswer(models.Model):
    id_user_tg = models.OneToOneField(
        User, models.CASCADE, to_field="id_user_tg", verbose_name='ID пользователя в телеграм'
    )
    id_user_quize = models.OneToOneField(UserQuize, models.CASCADE, verbose_name='ID запушеного пользователем теста')
    id_answer = models.OneToOneField(QuizeAnswer, models.CASCADE, verbose_name='ID ответа')
    question_number = models.IntegerField(blank=True, verbose_name="Номер вопроса")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        db_table = "user_answer"
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователя"
