# Generated by Django 4.1.7 on 2023-04-12 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предмет',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('content', models.JSONField(blank=True, verbose_name='Контент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('photo', models.FileField(blank=True, upload_to='video/%Y/%m/%d/', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='ФИО')),
                ('lesson', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='appForDiplom.lessons', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
    ]
