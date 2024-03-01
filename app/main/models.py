from django.db import models


class Acces(models.Model):
    level_text = models.CharField(max_length=200, unique=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Acces"
        verbose_name = "Доступ"
        verbose_name_plural = "Доступы"


class Constant(models.Model):
    id = models.AutoField(primary_key=True)
    constant_name = models.CharField(max_length=200, blank=True)
    constant_value = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "constant"
        verbose_name = "Константа"
        verbose_name_plural = "Константы"

    def __str__(self) -> str:
        return self.constant_name


class QuizeAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_quize = models.OneToOneField("Quize", models.CASCADE, unique=True, blank=True)
    question_number = models.IntegerField(blank=True)
    answer_number = models.IntegerField(blank=True)
    answer_text = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "quize_answer"
        verbose_name = "Ответ теста"
        verbose_name_plural = "Ответы теста"


class QuizeQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    id_quize = models.OneToOneField("Quize", models.CASCADE, unique=True, blank=True)
    question_number = models.IntegerField(blank=True)
    question_text = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "quize_question"
        verbose_name = "Вопрос теста"
        verbose_name_plural = "Вопросы теста"


class QuizeStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status_text = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "quize_qtatus"
        verbose_name = "Статус теста"
        verbose_name_plural = "Статусы теста"

    def __str__(self) -> str:
        return self.status_text


class QuizeTrueAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_quize = models.OneToOneField("Quize", models.CASCADE, unique=True, blank=True)
    id_answer = models.OneToOneField(
        QuizeAnswer, models.CASCADE, unique=True, blank=True
    )
    question_number = models.IntegerField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "quize_true_answer"
        verbose_name = "Правильный вопрос для теста"
        verbose_name_plural = "Правильные вопросы для теста"


class Quize(models.Model):
    id = models.AutoField(primary_key=True)
    quize_name = models.CharField(max_length=200, blank=True)
    quize_description = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "quize"
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self) -> str:
        return self.quize_name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    id_user_tg = models.BigIntegerField(unique=True, blank=True)
    user_login = models.CharField(max_length=200, blank=True)
    user_full_name = models.CharField(max_length=200, blank=True)
    user_level = models.OneToOneField("UserLevel", models.CASCADE, unique=True)
    user_access = models.OneToOneField("Acces", models.CASCADE, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь в telegramm"
        verbose_name_plural = "Пользователи в telegramm"

    def __str__(self) -> str:
        return f'{self.id_user_tg} {self.user_login}'


class UserAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    id_user_tg = models.OneToOneField(
        User, models.CASCADE, unique=True, to_field="id_user_tg"
    )
    id_user_quize = models.OneToOneField(
        "UserQuize", models.CASCADE, unique=True, to_field="id"
    )
    id_answer = models.OneToOneField(QuizeAnswer, models.CASCADE, unique=True)
    question_number = models.IntegerField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_answer"
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователя"


class UserLevel(models.Model):
    id = models.AutoField(primary_key=True)
    level_text = models.CharField(max_length=200, blank=True)
    min_level_score = models.IntegerField(blank=True)
    max_level_score = models.IntegerField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_level"
        verbose_name = "Уровень пользователя"
        verbose_name_plural = "Уровни пользователя"


class UserQuize(models.Model):
    id = models.AutoField(primary_key=True)
    id_user_tg = models.OneToOneField(
        User, models.CASCADE, unique=True, to_field="id_user_tg"
    )
    id_quize = models.OneToOneField(Quize, models.CASCADE, unique=True)
    quize_status = models.OneToOneField(QuizeStatus, models.CASCADE, unique=True)
    question_number = models.IntegerField(blank=True)
    id_answer_last = models.IntegerField(blank=True)
    quize_score = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_quize"
        verbose_name = "Запущенный тест пользователя"
        verbose_name_plural = "Запущенные тесты пользователя"
