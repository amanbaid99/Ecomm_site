# Generated by Django 3.0.3 on 2020-08-27 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0013_auto_20200827_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='dish_name',
            new_name='name',
        ),
    ]