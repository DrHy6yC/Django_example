# Generated by Django 4.2.10 on 2024-03-01 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_create_time_acces_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constant',
            name='constant_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='constant',
            name='constant_value',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='constant',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='constant',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='constant',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='quize',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quize',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quize',
            name='quize_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='quize',
            name='quize_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='quize',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='answer_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='answer_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='id_quize',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quize'),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='question_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='quizeanswer',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='id_quize',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quize'),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='question_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='question_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='quizequestion',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='quizestatus',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quizestatus',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quizestatus',
            name='status_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='quizestatus',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='id_answer',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quizeanswer'),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='id_quize',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.quize'),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='question_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='quizetrueanswer',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_user_tg',
            field=models.BigIntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_access',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.acces'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_full_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.userlevel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_login',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='id_answer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.quizeanswer'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='id_user_quize',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.userquize'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='id_user_tg',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.user', to_field='id_user_tg'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='level_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='max_level_score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='min_level_score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='id_answer_last',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='id_quize',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.quize'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='id_user_tg',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.user', to_field='id_user_tg'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='question_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='quize_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='quize_status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.quizestatus'),
        ),
        migrations.AlterField(
            model_name='userquize',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]