# Generated by Django 4.2.5 on 2023-09-30 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_alter_job_hiring_manager_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='hiring_manager_phone',
        ),
    ]