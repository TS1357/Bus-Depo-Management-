# Generated by Django 4.0.2 on 2022-04-05 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bus', '0005_bookbus_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookbus',
            name='date',
            field=models.DateField(default=datetime.date(2022, 4, 6)),
        ),
    ]
