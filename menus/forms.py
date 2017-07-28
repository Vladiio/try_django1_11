from django import forms

from restaurants.models import RestaurantLocation
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = [
            'restaurants',
            'name',
            'contents',
            'excludes',
            'publick',
        ]

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        super().__init__(*args, **kwargs)
        qs = RestaurantLocation.objects.filter(owner=user)#.exclude(item__isnull=False)
        self.fields['restaurants'].queryset = qs
