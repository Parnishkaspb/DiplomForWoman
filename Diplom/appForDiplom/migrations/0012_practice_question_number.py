# Generated by Django 4.1.7 on 2023-05-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appForDiplom', '0011_rename_id_video_teacher_lessons_test_id_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название практики')),
                ('number', models.IntegerField(default=10, verbose_name='Максимальное количество баллов')),
                ('practice', models.FileField(blank=True, upload_to='practice/%Y/%m/%d/', verbose_name='Файл с правильными запросами')),
            ],
            options={
                'verbose_name': 'Практика',
                'verbose_name_plural': 'Практики',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=10, verbose_name='Максимальное количество баллов'),
        ),
    ]
