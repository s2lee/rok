# Generated by Django 3.0.3 on 2020-08-02 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_ranker_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranker',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
