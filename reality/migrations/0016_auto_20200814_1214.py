# Generated by Django 3.0.3 on 2020-08-14 03:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reality', '0015_auto_20200814_1054'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='RealityUser',
        ),
    ]