# Generated by Django 2.2.1 on 2020-10-30 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20190511_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='address2',
        ),
    ]
