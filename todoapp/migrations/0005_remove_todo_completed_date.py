# Generated by Django 5.1.2 on 2024-10-22 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_rename_createddate_todo_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completed_date',
        ),
    ]
