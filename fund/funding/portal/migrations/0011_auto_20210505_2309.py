# Generated by Django 3.1.4 on 2021-05-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20210505_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='stdacd',
            name='Agentid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stdacd',
            name='Agentmail',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stdcour',
            name='Agentid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stdcour',
            name='Agentmail',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stdpro',
            name='Agentid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stdpro',
            name='Agentmail',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stdpro1',
            name='Agentid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stdpro1',
            name='Agentmail',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
