# Generated by Django 3.1.4 on 2021-05-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0023_auto_20210529_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Superadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=500)),
                ('Phonenumber', models.CharField(max_length=500, null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=500, null=True)),
                ('Confirmpassword', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]