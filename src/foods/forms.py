from django import forms

from accounts.forms import CSS_CLASS
from .models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = '__all__'
        exclude = ["user", "foods"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": CSS_CLASS})