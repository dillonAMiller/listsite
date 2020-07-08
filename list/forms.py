from django import forms
from .models import item

is_displayed_y_n = (
        ('0', 'No'),
        ('1', 'Yes'),
)
'''
class is_displayed_form(forms.ModelForm):
    error_css_class = 'error'

    is_displayed = forms.ChoiceField(choices=is_displayed_y_n, required=True)

    class Meta:
        model = item
'''
        