from django.db import models

class Users(models.Model):
    USER_TG_ID = models.BigIntegerField(unique=True)
    USER_LOGIN = models.CharField(max_length=200, unique=True)
    USER_FULL_NAME = models.CharField(max_length=256)
    USER_LEVEL = models.SmallIntegerField()
    USER_ACCESS = models.SmallIntegerField()
    CREATE_TIME = models.DateTimeField()
    UPDATE_TIME = models.DateTimeField()

    class Meta:
        db_table = 'USERS'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
