# Generated by Django 3.0.3 on 2020-07-13 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseon', '0006_auto_20200713_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=600),
        ),
    ]