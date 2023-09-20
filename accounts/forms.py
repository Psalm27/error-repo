from django import forms
from django.contrib.auth.forms import UserCreationForm

from industry.models import Type
from .models import CustomUser, Student, LevelChoices


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    index_number = forms.CharField(label='Index Number', max_length=15)
    level = forms.ChoiceField(label='Level', choices=LevelChoices)


class OrganizationRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    name = forms.CharField(label='Organization Name', max_length=100)
    industry_type = forms.ModelChoiceField(label='Industry Type', queryset=Type.objects.all())
    logo = forms.ImageField(label='Logo', required=False)
