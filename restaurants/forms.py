from django import forms

from .models import RestaurantLocation
from .validators import validate_category


class RestaurantLocationCreateForm(forms.ModelForm):
    # email = forms.EmailField()
    #category = forms.CharField(required=False, validators=[validate_category])

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if "edu" in email:
    #         raise forms.ValidationError("We do not accept edu emails")
    #     return email

    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
        ]


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
