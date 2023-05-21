# Generated by Django 4.1.7 on 2023-05-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appForDiplom', '0005_remove_teacher_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField(verbose_name='ID_преподавателя')),
                ('lesson_id', models.IntegerField(verbose_name='ID_урока')),
            ],
        ),
    ]
