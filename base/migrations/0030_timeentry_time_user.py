# Generated by Django 4.1.7 on 2023-05-15 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0029_remove_timeentry_days_remove_timeentry_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeentry',
            name='time_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
