# Generated by Django 2.2.3 on 2019-07-02 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20190702_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='conf',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='div',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='home',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='last',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='non_conf',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='road',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='streak',
        ),
    ]
