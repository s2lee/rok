# Generated by Django 3.0.3 on 2020-04-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20200405_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='keyname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='keystock',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]