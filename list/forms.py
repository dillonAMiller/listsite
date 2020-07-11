from django import forms
from .models import item

item_is_displayed_y_n = (
        ('0', 'No'),
        ('1', 'Yes'),
)

class itemDisplayedForm(forms.Form):
        item_is_displayed = forms.ChoiceField(choices = item_is_displayed_y_n, 
        label="Is Displayed", widget=forms.Select())
        