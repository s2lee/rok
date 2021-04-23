# Generated by Django 3.0.3 on 2020-04-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_delete_bookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('url', models.URLField(unique=True, verbose_name='url')),
            ],
        ),
    ]
