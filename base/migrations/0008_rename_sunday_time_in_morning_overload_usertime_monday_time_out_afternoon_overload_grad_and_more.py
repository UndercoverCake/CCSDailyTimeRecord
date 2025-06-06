# Generated by Django 4.1.7 on 2023-04-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_usertime_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertime',
            old_name='sunday_time_in_morning_overload',
            new_name='monday_time_out_afternoon_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='friday_time_in_afternoon_overload',
            new_name='monday_time_out_afternoon_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='friday_time_in_morning_overload',
            new_name='monday_time_out_morning_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='friday_time_out_afternoon_overload',
            new_name='monday_time_out_morning_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='friday_time_out_morning_overload',
            new_name='saturday_time_in_afternoon_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='monday_time_in_afternoon_overload',
            new_name='saturday_time_in_afternoon_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='monday_time_in_morning_overload',
            new_name='saturday_time_in_morning_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='monday_time_out_morning_overload',
            new_name='saturday_time_in_morning_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='monday_time_out_afternoon_overload',
            new_name='saturday_time_out_afternoon_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='saturday_time_in_afternoon_overload',
            new_name='saturday_time_out_afternoon_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='saturday_time_in_morning_overload',
            new_name='saturday_time_out_morning_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='saturday_time_out_afternoon_overload',
            new_name='saturday_time_out_morning_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='saturday_time_out_morning_overload',
            new_name='sunday_time_in_afternoon_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='sunday_time_in_afternoon_overload',
            new_name='sunday_time_in_afternoon_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='sunday_time_out_morning_overload',
            new_name='sunday_time_in_morning_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='sunday_time_out_afternoon_overload',
            new_name='sunday_time_in_morning_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='thursday_time_in_afternoon_overload',
            new_name='sunday_time_out_afternoon_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='thursday_time_in_morning_overload',
            new_name='sunday_time_out_afternoon_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='thursday_time_out_afternoon_overload',
            new_name='sunday_time_out_morning_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='tuesday_time_in_afternoon_overload',
            new_name='sunday_time_out_morning_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='thursday_time_out_morning_overload',
            new_name='thursday_time_in_afternoon_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='tuesday_time_in_morning_overload',
            new_name='thursday_time_in_afternoon_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='tuesday_time_out_afternoon_overload',
            new_name='thursday_time_in_morning_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='wednesday_time_in_afternoon_overload',
            new_name='thursday_time_in_morning_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='tuesday_time_out_morning_overload',
            new_name='thursday_time_out_afternoon_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='wednesday_time_in_morning_overload',
            new_name='thursday_time_out_afternoon_overload_undergrad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='wednesday_time_out_afternoon_overload',
            new_name='thursday_time_out_morning_overload_grad',
        ),
        migrations.RenameField(
            model_name='usertime',
            old_name='wednesday_time_out_morning_overload',
            new_name='thursday_time_out_morning_overload_undergrad',
        ),
        migrations.AddField(
            model_name='usertime',
            name='friday_time_in_afternoon_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='friday_time_in_afternoon_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='friday_time_in_morning_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='friday_time_in_morning_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='friday_time_out_afternoon_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='friday_time_out_afternoon_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='friday_time_out_morning_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='friday_time_out_morning_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='monday_time_in_afternoon_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='monday_time_in_afternoon_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='monday_time_in_morning_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='monday_time_in_morning_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='tuesday_time_in_afternoon_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='tuesday_time_in_afternoon_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='tuesday_time_in_morning_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='tuesday_time_in_morning_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='tuesday_time_out_afternoon_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='tuesday_time_out_afternoon_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='tuesday_time_out_morning_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='tuesday_time_out_morning_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='wednesday_time_in_afternoon_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='wednesday_time_in_afternoon_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='wednesday_time_in_morning_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='wednesday_time_in_morning_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='wednesday_time_out_afternoon_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='wednesday_time_out_afternoon_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='wednesday_time_out_morning_overload_grad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertime',
            name='wednesday_time_out_morning_overload_undergrad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
