# Generated by Django 3.0.3 on 2020-08-19 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joseon', '0026_auto_20200815_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='contents',
        ),
    ]
