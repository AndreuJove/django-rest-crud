# Generated by Django 4.0.5 on 2022-06-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_aircraft_serial_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="arrival_timestamp",
            field=models.DateTimeField(null=True),
        ),
    ]
