# Generated by Django 3.0.3 on 2020-04-14 05:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('joseon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='spear',
            field=models.ManyToManyField(blank=True, related_name='spear_post', to=settings.AUTH_USER_MODEL),
        ),
    ]