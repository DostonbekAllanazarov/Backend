# Generated by Django 4.2.1 on 2023-05-18 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0002_questions_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='user',
        ),
    ]
