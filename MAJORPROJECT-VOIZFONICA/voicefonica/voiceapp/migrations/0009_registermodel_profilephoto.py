# Generated by Django 3.2.7 on 2021-09-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voiceapp', '0008_auto_20210909_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='registermodel',
            name='profilephoto',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
