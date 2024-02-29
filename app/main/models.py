from django.db import models


class Acces(models.Model):
    LEVEL_TEXT = models.CharField(max_length=200, unique=True)
    CREATE_TIME = models.DateTimeField(auto_now_add=True)
    UPDATE_TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Acces"
        verbose_name = "Доступ"
        verbose_name_plural = "Доступы"


class Level(models.Model):
    LEVEL_TEXT = models.CharField(max_length=200, unique=True)
    MIN_LEVEL_SCORE = models.SmallIntegerField()
    MAX_LEVEL_SCORE = models.SmallIntegerField()
    CREATE_TIME = models.DateTimeField(auto_now_add=True)
    UPDATE_TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "LEVELS"
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"


class UserTG(models.Model):
    USER_TG_ID = models.BigIntegerField(unique=True)
    USER_LOGIN = models.CharField(max_length=200, unique=True)
    USER_FULL_NAME = models.CharField(max_length=256)
    USER_LEVEL = models.ForeignKey(to=Level, on_delete=models.CASCADE)
    USER_ACCESS = models.ForeignKey(to=Acces, on_delete=models.CASCADE)
    CREATE_TIME = models.DateTimeField(auto_now_add=True)
    UPDATE_TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "USER_TG"
        verbose_name = "Пользователь Телеграмм"
        verbose_name_plural = "Пользователи Телеграмм"
