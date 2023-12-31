# Generated by Django 4.1.5 on 2023-10-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(default=78.574729)),
                ('animalType', models.CharField(default='Animal', max_length=255)),
                ('lastSeen', models.TimeField(auto_now=True)),
            ],
        ),
    ]
