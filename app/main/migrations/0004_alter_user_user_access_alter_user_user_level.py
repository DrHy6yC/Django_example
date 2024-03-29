# Generated by Django 4.2.10 on 2024-03-03 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_quizetrueanswer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_access',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.accesuser', verbose_name='Доступ пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.leveluser', verbose_name='Уровень пользователя'),
        ),
    ]
