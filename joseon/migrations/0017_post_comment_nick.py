# Generated by Django 3.0.3 on 2020-07-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseon', '0016_comment_anonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_nick',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
