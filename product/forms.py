from django import forms
from .models import Item, Sku, Theme
from django.core import validators
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


#Custom validators
def pdf_url_ok(value):
    if value.endswith('.pdf') is False:
        if value.startswith('https://') is False:
            raise forms.ValidationError('File must be secure .pdf.')

def inventory_ok(value):
    if value < 0:
        raise forms.ValidationError('Must be positive inventory.')


# New Item form
class ItemForm(forms.ModelForm):

    item_number = forms.CharField(label='Item number XX0YYY:',
                                  validators=[RegexValidator('[+-/%#@]',
                                  inverse_match=True)],
                                  widget=forms.TextInput(attrs={
                                    'placeholder': 'XX0YYYY'
                                  }))

    
    item_instructions_url = forms.CharField(validators=[pdf_url_ok],
                                            widget=forms.URLInput(attrs={
                                            'placeholder': 'https:// ... .pdf'
                                            })
                                            )

    class Meta:
        model = Item
        fields = '__all__'


# New Sku form
class SkuForm(forms.ModelForm):

    class Meta:
        model = Sku
        fields = '__all__'
