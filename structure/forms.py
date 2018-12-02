from django import forms
from structure.models import Customer_Account, Country, Clan


class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Customer_Account
        fields = ['account_name', 'world']

class CreateCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_name']

class CreateClanForm(forms.ModelForm):
    class Meta:
        model = Clan
        fields = ['clan_name', 'country']