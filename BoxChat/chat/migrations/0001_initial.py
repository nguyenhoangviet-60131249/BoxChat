# Generated by Django 2.2.1 on 2019-05-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('chat', models.CharField(max_length=5000)),
                ('roomid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(default='', max_length=20, unique=True)),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('contact', models.BigIntegerField()),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
