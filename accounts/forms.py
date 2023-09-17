# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import Student, Organization, CustomUser
#
#
# class UserLoginForm(AuthenticationForm):
#     pass
#
#
# class StudentRegistrationForm(UserCreationForm):
#     passwordconfirm = forms.CharField(
#         label='Confirm Password',
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Confirm Password',
#             'class': 'form-control',
#         })
#     )
#
#     class Meta:
#         model = Student
#         fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'index_number', 'level', 'course', 'school')
#
#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control'}),
#             'index_number': forms.TextInput(attrs={'placeholder': 'Enter Index Number', 'class': 'form-control'}),
#             'level': forms.Select(attrs={'placeholder': 'Select Level', 'class': 'form-control'}),
#             'course': forms.Select(attrs={'placeholder': 'Select Course', 'class': 'form-control'}),
#             'school': forms.Select(attrs={'placeholder': 'Select School', 'class': 'form-control'}),
#         }
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password1')
#         passwordconfirm = cleaned_data.get('passwordconfirm')
#
#         if password != passwordconfirm:
#             raise forms.ValidationError('Passwords do not match')
#
#
#
#
# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#
#
# class OrganizationRegistrationForm(UserCreationForm):
#     passwordconfirm = forms.CharField(
#         label='Confirm Password',
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Confirm Password',
#             'class': 'form-control',
#         })
#     )
#
#     class Meta:
#         model = Organization
#         fields = UserCreationForm.Meta.fields + ['name', 'industry_type']
#
#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
#             'name': forms.TextInput(attrs={'placeholder': 'Enter name', 'class': 'form-control'}),
#             'industry_type': forms.TextInput(attrs={'placeholder': 'Enter industry_type', 'class': 'form-control'}),
#         }
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password1')
#         passwordconfirm = cleaned_data.get('passwordconfirm')
#
#         if password != passwordconfirm:
#             raise forms.ValidationError('Passwords do not match')