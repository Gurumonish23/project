# Generated by Django 3.1.5 on 2021-05-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0021_auto_20210528_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='stdappli',
            name='pstatus',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
