# Generated by Django 3.0.3 on 2020-07-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crazylab', '0007_post_apple'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(null=True),
        ),
    ]