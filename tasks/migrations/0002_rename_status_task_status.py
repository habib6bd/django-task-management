# Generated by Django 5.1.4 on 2025-01-26 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Status',
            new_name='status',
        ),
    ]
