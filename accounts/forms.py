from django import forms
from .models import Student, Organization, CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email']


class StudentRegistrationForm(CustomUserForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
        'label': 'Password',
    }))
    passwordconfirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'label': 'Confirm Password',  # Add a label for the password confirmation field
    }))

    class Meta(CustomUserForm.Meta):
        model = Student
        fields = CustomUserForm.Meta.fields + ['first_name', 'last_name', 'index_number', 'level', 'course', 'school']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        passwordconfirm = cleaned_data.get('passwordconfirm')

        if password != passwordconfirm:
            raise forms.ValidationError('Passwords do not match')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['index_number'].widget.attrs['placeholder'] = 'Enter Index Number'
        self.fields['level'].widget.attrs['placeholder'] = 'Select Level'
        self.fields['course'].widget.attrs['placeholder'] = 'Select Course'
        self.fields['school'].widget.attrs['placeholder'] = 'Select School'


#
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['email', ]


class OrganizationRegistrationForm(CustomUserForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
        'label': 'Password',
    }))
    passwordconfirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'label': 'Confirm Password',
    }))

    class Meta(CustomUserForm.Meta):
        model = Organization
        fields = CustomUserForm.Meta.fields + ['name', 'industry_type', 'logo', 'is_organization']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        passwordconfirm = cleaned_data.get('passwordconfirm')

        if password != passwordconfirm:
            raise forms.ValidationError('Passwords do not match')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Organization Name'
        self.fields['industry_type'].widget.attrs['placeholder'] = 'Select Industry Type'
        self.fields['logo'].widget.attrs['placeholder'] = 'Upload Logo'


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)