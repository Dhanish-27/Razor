# Generated by Django 5.0.6 on 2024-06-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_houses_room_capacity_houses_room_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='Customer_booked',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]