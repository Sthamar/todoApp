# Generated by Django 5.1.2 on 2024-10-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0017_rename_date_end_todo_datecompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('completed', 'completed'), ('pending', 'pending')], default='pending', max_length=250),
        ),
    ]
