# Generated by Django 3.0.3 on 2020-03-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200325_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jprofile',
            name='rank',
            field=models.CharField(choices=[('18', '從九品'), ('17', '正九品'), ('16', '從八品\t'), ('15', '正八品'), ('14', '從七品'), ('13', '正七品'), ('12', '從六品'), ('11', '正六品'), ('10', '從五品'), ('9', '正五品'), ('8', '從四品'), ('7', '正四品'), ('6', '從三品'), ('5', '正三品'), ('4', '從二品'), ('3', '正二品'), ('2', '從一品'), ('1', '正一品')], default='18', max_length=50, null=True),
        ),
    ]
