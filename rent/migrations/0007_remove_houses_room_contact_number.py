# Generated by Django 5.0.6 on 2024-06-23 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0006_alter_houses_room_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houses',
            name='Room_contact_number',
        ),
    ]