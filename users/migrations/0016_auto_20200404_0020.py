# Generated by Django 3.0.3 on 2020-04-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_certificate_coin_item_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='blackcoin',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
