# Generated by Django 2.1.2 on 2018-11-01 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Goal', '0003_goal_is_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_time', models.DateField(verbose_name='打卡时间')),
                ('feeling', models.TextField(null=True, verbose_name='今日心情')),
                ('position', models.TextField(null=True, verbose_name='打卡定位')),
                ('img', models.ImageField(null=True, upload_to='', verbose_name='打卡配图')),
                ('status', models.BooleanField(default=True, verbose_name='打卡状态')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goal.Goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
        ),
    ]
