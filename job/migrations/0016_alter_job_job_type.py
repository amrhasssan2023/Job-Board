# Generated by Django 4.1.2 on 2023-07-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Pull-Time', 'Pull-Time'), ('Full-Time', 'Full-Time')], max_length=100),
        ),
    ]
