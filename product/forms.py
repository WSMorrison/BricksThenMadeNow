from django import forms
from .models import Item, Sku, Theme

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        theme = Theme.objects.all()
        