# Generated by Django 5.1.2 on 2024-10-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_todo_date_end_alter_todo_ceated_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='todo',
            name='ceated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]