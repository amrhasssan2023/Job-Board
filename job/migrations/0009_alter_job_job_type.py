# Generated by Django 4.1.2 on 2023-07-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full-Time', 'Full-Time'), ('Pull-Time', 'Pull-Time')], max_length=100),
        ),
    ]