# Generated by Django 3.0.3 on 2020-09-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0059_auto_20200903_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]