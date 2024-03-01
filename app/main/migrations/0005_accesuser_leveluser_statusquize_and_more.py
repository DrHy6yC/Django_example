# Generated by Django 4.2.10 on 2024-03-01 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_constant_options_alter_quize_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccesUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acces_text', models.CharField(blank=True, max_length=200, unique=True, verbose_name='Название доступа')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Доступ',
                'verbose_name_plural': 'Доступы',
                'db_table': 'acces_user',
            },
        ),
        migrations.CreateModel(
            name='LevelUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_text', models.CharField(blank=True, max_length=200, verbose_name='')),
                ('min_level_score', models.IntegerField(blank=True, verbose_name='')),
                ('max_level_score', models.IntegerField(blank=True, verbose_name='')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Уровень пользователя',
                'verbose_name_plural': 'Уровни пользователя',
                'db_table': 'level_user',
            },
        ),
        migrations.CreateModel(
            name='StatusQuize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(blank=True, max_length=200, verbose_name='')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Статус теста',
                'verbose_name_plural': 'Статусы теста',
                'db_table': 'status_quize',
            },
        ),
        migrations.AlterField(
            model_name='constant',
            name='constant_name',
            field=models.CharField(blank=True, max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='constant',
            name='constant_value',
            field=models.CharField(blank=True, max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quize',
            name='quize_description',
            field=models.CharField(blank=True, max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quize',
            name='quize_name',
            field=models.CharField(blank=True, max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='answer_number',
            field=models.IntegerField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='answer_text',
            field=models.CharField(blank=True, max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='id_quize',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quize', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='id_quize',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quize', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='question_text',
            field=models.CharField(blank=True, max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='id_answer',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quizeanswer', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='id_quize',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quize', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_user_tg',
            field=models.BigIntegerField(blank=True, unique=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_full_name',
            field=models.CharField(blank=True, max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_login',
            field=models.CharField(blank=True, max_length=200, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='id_answer_last',
            field=models.IntegerField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='question_number',
            field=models.IntegerField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_access',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.accesuser'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.leveluser'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='quize_status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.statusquize'),
        ),
        migrations.DeleteModel(
            name='Acces',
        ),
        migrations.DeleteModel(
            name='QuizeStatus',
        ),
        migrations.DeleteModel(
            name='UserLevel',
        ),
    ]
