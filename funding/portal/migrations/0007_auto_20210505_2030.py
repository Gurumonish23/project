# Generated by Django 3.1.4 on 2021-05-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_consultancy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Consultancy',
        ),
        migrations.AlterField(
            model_name='agent',
            name='Firstname',
            field=models.CharField(max_length=50),
        ),
    ]
