# Generated by Django 3.1.5 on 2021-06-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0030_auto_20210605_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultancydetails',
            name='Rbody',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='consultancydetails',
            name='Rno',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
