# Generated by Django 3.1.4 on 2021-05-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0020_auto_20210528_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stdappli',
            name='id',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
