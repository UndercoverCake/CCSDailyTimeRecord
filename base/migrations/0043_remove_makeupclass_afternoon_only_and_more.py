# Generated by Django 4.1.7 on 2023-05-18 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_makeupclass_afternoon_time_in_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makeupclass',
            name='afternoon_only',
        ),
        migrations.RemoveField(
            model_name='makeupclass',
            name='morning_only',
        ),
    ]
