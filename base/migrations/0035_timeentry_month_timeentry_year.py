# Generated by Django 4.1.7 on 2023-05-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_timeentry_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeentry',
            name='month',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='timeentry',
            name='year',
            field=models.IntegerField(default=2023),
        ),
    ]
