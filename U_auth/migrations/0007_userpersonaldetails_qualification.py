# Generated by Django 5.0.8 on 2024-08-26 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0006_costume_user_is_online_additionaldetails_job_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpersonaldetails',
            name='qualification',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
