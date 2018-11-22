from django import forms
from structure.models import Customer_Account


class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Customer_Account
        fields = ['name', 'world']

 #   name = forms.CharField(required=True)
 #   world = forms.EmailField(required=True)