# Generated by Django 5.1.4 on 2025-02-13 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_taskdetail_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
    ]
