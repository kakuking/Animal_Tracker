# Generated by Django 4.1.5 on 2023-10-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_sighting_longitude_alter_sighting_latitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='lastSeen',
        ),
        migrations.AddField(
            model_name='sighting',
            name='dateTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
