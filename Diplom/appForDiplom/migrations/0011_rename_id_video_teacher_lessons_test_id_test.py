# Generated by Django 4.1.7 on 2023-05-30 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appForDiplom', '0010_teacher_lessons_test_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher_lessons_test',
            old_name='id_video',
            new_name='id_test',
        ),
    ]
