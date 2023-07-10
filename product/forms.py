from django import forms
from .models import Item, Sku, Theme
from django.core import validators
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


#Custom validators
def pdf_url_ok(value):
    if value.endswith('.pdf') is False:
        if value.startswith('https://') is False:
            raise forms.ValidationError('File must be secure .pdf')


# New Item form
class ItemForm(forms.ModelForm):

    item_number = forms.CharField(label='Item number XX0YYY:',
                                  validators=[RegexValidator('[+-/%#@]',
                                  inverse_match=True)],
                                  widget=forms.TextInput(attrs={
                                    'placeholder': 'XX: year created - 0 - YYYY Lego ref number'
                                  }))

    
    item_instructions_url = forms.CharField(label='Downloadable .pdf link',
                                            validators=[pdf_url_ok],
                                            widget=forms.URLInput(attrs={
                                            'placeholder': 'https://...pdf'
                                            })
                                            )

    class Meta:
        model = Item
        fields = '__all__'
        labels = {'item_name': 'Item name; use the original Lego set name:',    
                  'item_theme': 'Choose theme:',
                  'item_description': 'Brief item description; remember SEO keywords:',
                  'item_old_url': 'Image hosted link:',
                  'item_render_link': 'Render hosted link:',
                  'item_modern_link': 'Modern, corporeal image, where available, hosted link:',
                  'item_detail_url': 'Detail image hosted link:',
                  'item_part_count': 'How many Lego bricks and elements are used? Exclude minifigs:'
                  }


# New Sku form
class SkuForm(forms.ModelForm):

    class Meta:
        model = Sku
        fields = '__all__'
