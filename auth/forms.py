from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['first_name']

        if commit:
            user.save()

        return user







""" TEST
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
"""
