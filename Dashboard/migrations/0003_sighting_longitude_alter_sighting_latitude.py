# Generated by Django 4.1.5 on 2023-10-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_animal_alter_sighting_animaltype'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='longitude',
            field=models.FloatField(default=78.574729),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='latitude',
            field=models.FloatField(default=17.54361),
        ),
    ]