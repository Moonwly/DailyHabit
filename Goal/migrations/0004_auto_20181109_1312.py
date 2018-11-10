# Generated by Django 2.1.2 on 2018-11-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goal', '0003_goal_is_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='repeat_time',
            field=models.CharField(default='MON, TUE, WED, THU, FRI, SAT, SUN,', max_length=255, null=True, verbose_name='重复时间'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='total_day',
            field=models.IntegerField(default=-1, verbose_name='总天数'),
        ),
    ]