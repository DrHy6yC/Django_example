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


class QuizeQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    id_quize = models.OneToOneField("Quize", models.CASCADE, unique=True, blank=True)
    question_number = models.IntegerField(blank=True)
    question_text = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "quize_question"


class QuizeStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status_text = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "quize_qtatus"

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


class Quize(models.Model):
    id = models.AutoField(primary_key=True)
    quize_name = models.CharField(max_length=200, blank=True)
    quize_description = models.CharField(max_length=200, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "quize"

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


class UserLevel(models.Model):
    id = models.AutoField(primary_key=True)
    level_text = models.CharField(max_length=200, blank=True)
    min_level_score = models.IntegerField(blank=True)
    max_level_score = models.IntegerField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_level"


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
