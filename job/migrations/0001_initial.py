# Generated by Django 4.1.2 on 2023-07-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('job_type', models.CharField(choices=[('Pull-Time', 'Pull-Time'), ('Full-Time', 'Full-Time')], max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('vacancy', models.IntegerField(default=1)),
                ('salary', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=1)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
