from django import forms
from .models import SiteUser

class SiteUserform(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = {'siteuser_phone_number',
                  'siteuser_street_address1',
                  'siteuser_street_address2',
                  'siteuser_town_or_city',
                  'siteuser_state',
                  'siteuser_zipcode',
                  'siteuser_country',
                  }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'siteuser_phone_number': 'Phone Number',
            'siteuser_street_address1': 'Street Address 1',
            'siteuser_street_address2': 'Street Address 2',
            'siteuser_town_or_city': 'Town or City',
            'siteuser_state': 'State',
            'siteuser_zipcode': 'ZIP',
            'siteuser_country': 'Country',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
