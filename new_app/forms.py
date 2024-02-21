from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User


from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from new_app.models import Register, Publisher, Customer, blog


class CustomUserForm(UserCreationForm):
    class Meta:
        model = Register
        fields = ('username','email','first_name','last_name',)

class DateInput(forms.DateInput):
    input_type='date'

class RegistrationForm(UserCreationForm):
    Username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ('username','password1','password2')





class PublisherForm(forms.ModelForm):
    ph_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Must be in the format: '9999999999'")
    phone = forms.CharField(validators=[ph_regex])

    class Meta:
        model = Publisher
        fields = ('name','phone','email',)


class CustomerForm(forms.ModelForm):
    ph_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Must be in the format: '9999999999'")
    phone = forms.CharField(validators=[ph_regex])


    class Meta:
        model = Customer
        fields = ('phone','address','name',)



class BlogForm(forms.ModelForm):
    class Meta:
        model=blog
        fields='__all__'
