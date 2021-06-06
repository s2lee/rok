# Generated by Django 3.0.3 on 2020-07-28 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joseon', '0012_post_anonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='nickname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='joseon_comment_anonymous', to='joseon.Post'),
        ),
    ]