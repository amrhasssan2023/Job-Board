# Generated by Django 4.1.2 on 2023-07-10 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_job_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
    ]