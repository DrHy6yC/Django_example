from django.db import models


class Acces(models.Model):
    LEVEL_TEXT = models.CharField(max_length=200, unique=True)
    CREATE_TIME = models.DateTimeField(auto_now_add=True)
    UPDATE_TIME = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Acces"
        verbose_name = "Доступ"
        verbose_name_plural = "Доступы"


class Constant(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    constant_name = models.CharField(max_length=200, db_column='constant_name')
    constant_value = models.CharField(max_length=200, db_column='constant_value')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'constant'


class QuizeAnswer(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    id_quize = models.OneToOneField('Quize', models.CASCADE, unique=True, db_column='id_quize')
    question_number = models.IntegerField(db_column='question_number')
    answer_number = models.IntegerField(db_column='answer_number')
    answer_text = models.CharField(max_length=200, db_column='answer_text')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'quize_answer'


class QuizeQuestion(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    id_quize = models.OneToOneField('Quize', models.CASCADE, unique=True, db_column='id_quize')
    question_number = models.IntegerField(db_column='question_number')
    question_text = models.CharField(max_length=200, db_column='question_text')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'quize_question'


class QuizeStatus(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    status_text = models.CharField(max_length=200, db_column='status_text')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'quize_qtatus'


class QuizeTrueAnswer(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    id_quize = models.OneToOneField('Quize', models.CASCADE, unique=True, db_column='id_quize')
    id_answer = models.OneToOneField(QuizeAnswer, models.CASCADE, unique=True, db_column='id_answer')
    question_number = models.IntegerField(db_column='question_number')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'quize_true_answer'


class Quize(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    quize_name = models.CharField(max_length=200, db_column='quize_name')
    quize_description = models.CharField(max_length=200, db_column='quize_description')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'quize'


class User(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    id_user_tg = models.BigIntegerField(db_column='id_user_tg', unique=True)
    user_login = models.CharField(max_length=200, db_column='user_login')
    user_full_name = models.CharField(max_length=200, db_column='user_full_name')
    user_level = models.OneToOneField('UserLevel', models.CASCADE, unique=True, db_column='user_level')
    user_access = models.IntegerField(db_column='user_access')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'user'


class UserAnswer(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    id_user_tg = models.OneToOneField(User, models.CASCADE, unique=True, db_column='id_user_tg', to_field='id_user_tg')
    id_user_quize = models.OneToOneField('UserQuize', models.CASCADE, unique=True, db_column='id_user_quize', to_field='id')
    id_answer = models.OneToOneField(QuizeAnswer, models.CASCADE, unique=True, db_column='id_answer')
    question_number = models.IntegerField(db_column='question_number')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'user_answer'


class UserLevel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    level_text = models.CharField(max_length=200, db_column='level_text')
    min_level_score = models.IntegerField(db_column='min_level_score')
    max_level_score = models.IntegerField(db_column='max_level_score')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'user_level'


class UserQuize(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    id_user_tg = models.OneToOneField(User, models.CASCADE, unique=True, db_column='id_user_tg', to_field='id_user_tg')
    id_quize = models.OneToOneField(Quize, models.CASCADE, unique=True, db_column='id_quize')
    quize_status = models.OneToOneField(QuizeStatus, models.CASCADE, unique=True, db_column='quize_status')
    question_number = models.IntegerField(db_column='question_number')
    id_answer_last = models.IntegerField(db_column='id_answer_last')
    quize_score = models.IntegerField(db_column='quize_score')
    create_time = models.DateTimeField(db_column='create_time')
    update_time = models.DateTimeField(db_column='update_time')

    class Meta:
        db_table = 'user_quize'
