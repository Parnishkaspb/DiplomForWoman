# Generated by Django 4.1.7 on 2023-06-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appForDiplom', '0013_practice_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.TextField(blank=True, verbose_name='Видео'),
        ),
    ]