# Generated by Django 4.1.5 on 2023-11-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_alter_sighting_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='id_submitted',
            field=models.CharField(default='2020ABCD0001H', max_length=13),
        ),
    ]
