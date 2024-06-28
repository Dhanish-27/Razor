# Generated by Django 5.0.6 on 2024-06-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_img', models.ImageField(upload_to='rooms')),
                ('Room_name', models.CharField(max_length=20)),
                ('Room_size', models.IntegerField()),
                ('Room_count', models.IntegerField()),
                ('Room_amentities', models.TextField()),
                ('Room_description', models.TextField()),
                ('Room_priceperday', models.FloatField()),
                ('Room_maximumstay', models.IntegerField()),
                ('Room_minimumstay', models.IntegerField()),
                ('Room_is_booked', models.BooleanField(default=False)),
            ],
        ),
    ]