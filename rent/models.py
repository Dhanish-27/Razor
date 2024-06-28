from django.db import models

# Create your models here.
class houses(models.Model):
    Room_img=models.ImageField(upload_to="rooms")
    Room_name=models.CharField(max_length=20)
    Room_size=models.IntegerField()
    Room_count=models.IntegerField()
    Room_amentities=models.TextField()
    Room_description=models.TextField()
    Room_priceperday=models.FloatField()
    Room_maximumstay=models.IntegerField()
    Room_minimumstay=models.IntegerField()
    Room_capacity=models.CharField(max_length=40)
    Room_location=models.CharField(max_length=20)
    Room_is_booked=models.BooleanField(default=False)
    Room_servicesincluded=models.BooleanField(default=True)
    Room_foodincluded=models.BooleanField(default=True)
    Customer_booked=models.CharField(max_length=20)
    # Room_contact_number=models.IntegerField()