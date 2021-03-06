# Generated by Django 2.2.3 on 2019-07-02 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('win', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('pf', models.IntegerField()),
                ('pa', models.IntegerField()),
                ('net_pts', models.IntegerField()),
                ('home', models.SmallIntegerField()),
                ('road', models.SmallIntegerField()),
                ('div', models.SmallIntegerField()),
                ('conf', models.SmallIntegerField()),
                ('pct', models.DecimalField(decimal_places=3, max_digits=4)),
                ('non_conf', models.SmallIntegerField()),
                ('streak', models.SmallIntegerField()),
                ('last', models.SmallIntegerField()),
            ],
        ),
    ]
