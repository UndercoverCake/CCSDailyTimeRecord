# Generated by Django 4.1.7 on 2023-05-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_usertime_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertime',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
