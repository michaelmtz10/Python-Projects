# Generated by Django 2.0.7 on 2021-08-31 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0006_auto_20210828_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='title',
            field=models.CharField(choices=[('science', 'science'), ('english', 'english'), ('history', 'history'), ('math', 'math')], max_length=60),
        ),
    ]
