# Generated by Django 4.1.7 on 2023-06-03 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appForDiplom', '0016_alter_question_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО студента')),
            ],
        ),
        migrations.CreateModel(
            name='User_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='ID студента')),
                ('id_test', models.IntegerField(verbose_name='ID теста')),
                ('json_massive', models.TextField(verbose_name='JSON_массив с информацией об тесте')),
            ],
        ),
    ]
