# Generated by Django 5.1.2 on 2024-10-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_todo_ceated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='ceated_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
