# Generated by Django 3.1.4 on 2021-05-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_delete_nanda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=500)),
                ('Phonenumber', models.CharField(max_length=500)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=500)),
                ('Confirmpassword', models.CharField(max_length=500)),
            ],
        ),
    ]
