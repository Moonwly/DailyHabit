# Generated by Django 2.1.2 on 2018-11-01 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Record', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='feeling',
            new_name='record_feeling',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='img',
            new_name='record_image',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='position',
            new_name='record_position',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='status',
            new_name='record_status',
        ),
    ]