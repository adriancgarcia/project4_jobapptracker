# Generated by Django 4.2.5 on 2023-09-28 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_job_date_applied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_applied',
            field=models.CharField(max_length=200),
        ),
    ]
