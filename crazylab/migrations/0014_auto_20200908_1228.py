# Generated by Django 3.0.3 on 2020-09-08 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crazylab', '0013_auto_20200815_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='contents',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='down',
        ),
    ]
