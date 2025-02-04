from django import forms

from accounts.forms import CSS_CLASS
from .models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = '__all__'
        exclude = ["user", "foods"]