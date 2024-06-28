# Generated by Django 5.0.6 on 2024-06-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_houses_customer_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='Room_contact_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_amentities',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_capacity',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_foodincluded',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_is_booked',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_location',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_maximumstay',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_minimumstay',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_priceperday',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_servicesincluded',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='houses',
            name='Room_size',
            field=models.IntegerField(null=True),
        ),
    ]