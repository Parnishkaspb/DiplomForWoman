# Generated by Django 4.1.7 on 2023-05-17 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appForDiplom', '0004_alter_videos_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='lesson',
        ),
    ]
