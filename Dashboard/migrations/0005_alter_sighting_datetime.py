# Generated by Django 4.1.5 on 2023-10-18 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_remove_sighting_lastseen_sighting_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
