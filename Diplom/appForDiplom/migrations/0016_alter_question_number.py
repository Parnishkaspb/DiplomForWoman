# Generated by Django 4.1.7 on 2023-06-03 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appForDiplom', '0015_remove_question_a_question_a_1_question_a_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Максимальное количество баллов'),
        ),
    ]