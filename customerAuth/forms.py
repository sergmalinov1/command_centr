from django.forms import ModelForm
from django import forms
from customerAuth.models import Customer



class SignUpForm(ModelForm):
 #   first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
 #   last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
 #   email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Customer
        fields = ('customer_name', 'password')


class LoginForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name',)

 #   name = forms.CharField(max_length=100)
  #  password = forms.CharField(widget=forms.PasswordInput)


