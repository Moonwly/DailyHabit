# Generated by Django 2.1.2 on 2018-11-05 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Record', '0003_auto_20181105_0144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='record_time',
            new_name='record_date',
        ),
    ]
