# Generated by Django 3.0.3 on 2020-08-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=200)),
                ('specialities', models.CharField(max_length=200, null=True)),
                ('min_price_range', models.IntegerField()),
                ('max_price_range', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]