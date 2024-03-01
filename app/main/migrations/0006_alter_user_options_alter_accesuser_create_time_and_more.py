# Generated by Django 4.2.10 on 2024-03-01 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_accesuser_leveluser_statusquize_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь в telegram', 'verbose_name_plural': 'Пользователи в telegram'},
        ),
        migrations.AlterField(
            model_name='accesuser',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='accesuser',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='constant',
            name='constant_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Наименование переменной'),
        ),
        migrations.AlterField(
            model_name='constant',
            name='constant_value',
            field=models.CharField(blank=True, max_length=200, verbose_name='Значение переменной'),
        ),
        migrations.AlterField(
            model_name='constant',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='constant',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='leveluser',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='leveluser',
            name='level_text',
            field=models.CharField(blank=True, max_length=200, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='leveluser',
            name='max_level_score',
            field=models.IntegerField(blank=True, verbose_name='Максимальный процент уровня'),
        ),
        migrations.AlterField(
            model_name='leveluser',
            name='min_level_score',
            field=models.IntegerField(blank=True, verbose_name='Минималтный процент уровня'),
        ),
        migrations.AlterField(
            model_name='leveluser',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='quize',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='quize',
            name='quize_description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Описание теста'),
        ),
        migrations.AlterField(
            model_name='quize',
            name='quize_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Имя теста'),
        ),
        migrations.AlterField(
            model_name='quize',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='answer_number',
            field=models.IntegerField(blank=True, verbose_name='Номер ответа'),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='answer_text',
            field=models.CharField(blank=True, max_length=200, verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='id_quize',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quize', verbose_name='ID теста'),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name='Номер вопроса'),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='id_quize',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quize', verbose_name='ID теста'),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name='Номер вопроса'),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='question_text',
            field=models.CharField(blank=True, max_length=200, verbose_name='Текст вопроса'),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='id_answer',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quizeanswer', verbose_name='ID ответа'),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='id_quize',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quize', verbose_name='ID теста'),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name='Номер вопроса'),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='statusquize',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='statusquize',
            name='status_text',
            field=models.CharField(blank=True, max_length=200, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='statusquize',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_user_tg',
            field=models.BigIntegerField(blank=True, unique=True, verbose_name='ID пользователя в телеграм'),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_access',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.accesuser', verbose_name='Доступ пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_full_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Полное имя и фамилия из телеграмм'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.leveluser', verbose_name='Уровень пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_login',
            field=models.CharField(blank=True, max_length=200, verbose_name='Лонин пользователя в телеграмм'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='id_answer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.quizeanswer', verbose_name='ID ответа'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='id_user_quize',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.userquize', verbose_name='ID запушеного пользователем теста'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='id_user_tg',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.user', to_field='id_user_tg', verbose_name='ID пользователя в телеграм'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name='Номер вопроса'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='id_answer_last',
            field=models.IntegerField(blank=True, verbose_name='ID последнего ответа пользователя'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='id_quize',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.quize', verbose_name='ID теста'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='id_user_tg',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.user', to_field='id_user_tg', verbose_name='ID пользователя в телеграмм'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name='Номер вопроса'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='quize_score',
            field=models.IntegerField(verbose_name='Количество баллов пользователя'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='quize_status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.statusquize', verbose_name='ID статуса теста'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]
