# Generated by Django 3.1.4 on 2021-05-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20210505_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Type', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
