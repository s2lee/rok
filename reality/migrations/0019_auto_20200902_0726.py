# Generated by Django 3.0.3 on 2020-09-01 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reality', '0018_auto_20200831_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='accused',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='accused',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
