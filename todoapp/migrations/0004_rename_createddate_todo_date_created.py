# Generated by Django 5.1.2 on 2024-10-22 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_rename_created_date_todo_createddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='createddate',
            new_name='date_created',
        ),
    ]
