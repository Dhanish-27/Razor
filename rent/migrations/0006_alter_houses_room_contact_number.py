# Generated by Django 5.0.6 on 2024-06-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_houses_room_contact_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='Room_contact_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
