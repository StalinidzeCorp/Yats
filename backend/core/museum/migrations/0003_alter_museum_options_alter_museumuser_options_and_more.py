# Generated by Django 5.0.3 on 2024-04-13 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0002_alter_museum_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='museum',
            options={'verbose_name': 'Музей', 'verbose_name_plural': 'Музеи'},
        ),
        migrations.AlterModelOptions(
            name='museumuser',
            options={'verbose_name': 'Сотрудник музея', 'verbose_name_plural': 'Сотрудники музеев'},
        ),
        migrations.AddField(
            model_name='museum',
            name='short_name',
            field=models.CharField(max_length=20, null=True, verbose_name='Аббревиатура'),
        ),
        migrations.AlterField(
            model_name='museum',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='museum',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='museum',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='museum',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='museum',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлен'),
        ),
        migrations.AlterField(
            model_name='museumuser',
            name='access_level',
            field=models.IntegerField(choices=[(0, 'Employee'), (1, 'Manager'), (2, 'Moderator'), (3, 'Administrator'), (4, 'Owner')], default=0, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='museumuser',
            name='joined_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Присоеденился'),
        ),
        migrations.AlterField(
            model_name='museumuser',
            name='museum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museum.museum', verbose_name='Музей'),
        ),
        migrations.AlterField(
            model_name='museumuser',
            name='position',
            field=models.CharField(default='Сотрудник', max_length=30, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='museumuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterUniqueTogether(
            name='museumuser',
            unique_together={('user', 'museum')},
        ),
    ]