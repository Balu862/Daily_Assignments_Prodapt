# Generated by Django 3.2.7 on 2021-09-08 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillPrepaidModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billnumber', models.IntegerField()),
                ('cid', models.IntegerField()),
                ('planid', models.IntegerField()),
                ('transactiontype', models.CharField(max_length=50)),
                ('pactivateddate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='PlansModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pvalidity', models.IntegerField()),
                ('pdata', models.IntegerField()),
                ('ptalktime', models.IntegerField()),
                ('service', models.CharField(max_length=50)),
                ('device', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostpaidDongleCustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('planid', models.IntegerField()),
                ('activatestatus', models.BooleanField()),
                ('pactivateddate', models.DateTimeField()),
                ('pexpirydate', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='PostpaidDonglePlansModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pvalidity', models.CharField(max_length=50)),
                ('pdata', models.CharField(max_length=50)),
                ('ptype', models.CharField(max_length=1000)),
                ('sms', models.CharField(max_length=1000)),
                ('subscription', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PrepaidDongleCustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('planid', models.IntegerField()),
                ('activatestatus', models.BooleanField()),
                ('pactivateddate', models.DateTimeField()),
                ('pexpirydate', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='PrepaidDonglePlansModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pvalidity', models.CharField(max_length=50)),
                ('pdata', models.CharField(max_length=50)),
                ('ptalktime', models.CharField(max_length=50)),
                ('ptype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PrepaidMobileCustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('planid', models.IntegerField()),
                ('activatestatus', models.BooleanField()),
                ('pactivateddate', models.DateTimeField()),
                ('pexpirydate', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='PrepaidMobilePlansModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pvalidity', models.IntegerField()),
                ('pdata', models.IntegerField()),
                ('ptalktime', models.IntegerField()),
                ('psms', models.IntegerField()),
                ('ptype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('device', models.CharField(max_length=50)),
                ('service', models.CharField(max_length=50)),
                ('aadhar', models.BigIntegerField()),
            ],
        ),
    ]
