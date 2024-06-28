from django import forms
from.models import houses

class HouseForm(forms.ModelForm):
    class Meta:
        model = houses
        fields = ('Room_name', 
                  'Room_location',
                  'Room_count', 
                  'Room_size', 
                  'Room_priceperday', 
                  'Room_img',
                  'Room_amentities',
                  'Room_description',
                  'Room_maximumstay',
                  'Room_minimumstay',
                  'Room_capacity',
                  'Room_is_booked',
                  'Room_servicesincluded',
                  'Room_foodincluded')
        labels={'Room_name':'Room_name',
                  'Room_location':'Room_location',
                  'Room_count':'Room_count',
                  'Room_size':'Room_size',
                  'Room_priceperday':'Room_priceperday',
                  'Room_img':'Room_img',
                  'Room_amentities':'Room_amentities',
                  'Room_description':'Room_description',
                  'Room_maximumstay':'Room_maximumstay',
                  'Room_minimumstay':'Room_minimumstay',
                  'Room_capacity':'Room_capacity',
                  'Room_is_booked':'Room_is_booked',
                  'Room_servicesincluded':'Room_servicesincluded',
                  'Room_foodincluded':'Room_foodincluded'

        }
        widgets = {
            'Room_description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }