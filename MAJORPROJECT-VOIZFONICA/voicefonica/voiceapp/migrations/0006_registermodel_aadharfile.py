# Generated by Django 3.2.6 on 2021-09-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voiceapp', '0005_auto_20210908_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='registermodel',
            name='aadharfile',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
