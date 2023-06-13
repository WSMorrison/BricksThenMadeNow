from django import forms
from .models import Item, Sku, Theme

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Layout, Field, MultiField, Div, Fieldset
from crispy_forms.bootstrap import InlineField

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        labels = {'item_number': 'Item number XX0YYYY; where XX is the two digit year BTMN generated the item, and YYYY is the original Lego item number (replace the 0 for five digit numbers):',
                  'item_name': 'Item name; use the original Lego set name:',
                  'item_theme': 'Choose theme:',
                  'item_description': 'Brief item description; remember SEO keywords:',
                  'item_old': 'Image of the reference set:',
                  'item_old_url': 'Image hosted link:',
                  'item_render': 'Render of BTMN version:',
                  'item_render_link': 'Render hosted link:',
                  'item_modern': 'Image of BTMN version built up, where available:',
                  'item_modern_link': 'Modern, corporeal image, where available, hosted link:',
                  'item_detail': 'Optional detail photo, render or corporeal',
                  'item_detail_url': 'Detail image hosted link:',
                  'item_part_count': 'How many Lego bricks and elements are used? Exclude minifigs:'
                  }

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        theme = Theme.objects.all()
        