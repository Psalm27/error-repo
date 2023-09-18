from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Student, Organization, CustomUser
from django.contrib.auth import get_user_model

class UserLoginForm(AuthenticationForm):
    pass


class StudentRegistrationForm(UserCreationForm):
    passwordconfirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control',
        })
    )

    class Meta:
        model = get_user_model()  # Use get_user_model() to reference your custom user model
        fields = ('email', 'password1', 'password2')  # Specify the fields you want to include in the form

    # Add any additional fields specific to the Student model here
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter First Name',
            'class': 'form-control',
        })
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Last Name',
            'class': 'form-control',
        })
    )
    index_number = forms.CharField(
        label='Index Number',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Index Number',
            'class': 'form-control',
        })
    )
    level = forms.CharField(
        label='Level',
        widget=forms.Select(attrs={
            'placeholder': 'Select Level',
            'class': 'form-control',
        })
    )
    course = forms.CharField(
        label='Course',
        widget=forms.Select(attrs={
            'placeholder': 'Select Course',
            'class': 'form-control',
        })
    )
    school = forms.CharField(
        label='School',
        widget=forms.Select(attrs={
            'placeholder': 'Select School',
            'class': 'form-control',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        passwordconfirm = cleaned_data.get('passwordconfirm')

        if password != passwordconfirm:
            raise forms.ValidationError('Passwords do not match')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class OrganizationRegistrationForm(UserCreationForm):
    passwordconfirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control',
        })
    )

    class Meta:
        model = Organization
        fields = ['name', 'industry_type']
        labels = {
            'username': 'Email',
        }

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter name', 'class': 'form-control'}),
            'industry_type': forms.TextInput(attrs={'placeholder': 'Enter industry_type', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        passwordconfirm = cleaned_data.get('passwordconfirm')

        if password != passwordconfirm:
            raise forms.ValidationError('Passwords do not match')
