# Generated by Django 4.1.7 on 2023-05-15 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_remove_timeentry_time_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TimeEntry',
        ),
    ]
