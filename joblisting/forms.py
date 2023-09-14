from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['job_title', 'job_description', 'job_role', 'job_location', 'job_responsibilities', 'salary', 'job_type', 'expired']

    def __init__(self, *args, **kwargs):
        super(JobPostingForm, self).__init__(*args, **kwargs)

        # You can add custom widget attributes or customize form fields here if needed
        self.fields['job_description'].widget = forms.Textarea(attrs={'rows': 5})
        self.fields['job_responsibilities'].widget = forms.Textarea(attrs={'rows': 5})

        # Customize the labels or placeholders if needed
        self.fields['job_title'].label = 'Job Title'
        self.fields['job_description'].label = 'Job Description'
        self.fields['job_role'].label = 'Job Role'
        self.fields['job_location'].label = 'Job Location'
        self.fields['job_responsibilities'].label = 'Job Responsibilities'
        self.fields['salary'].label = 'Salary'
        self.fields['job_type'].label = 'Job Type'
        self.fields['expired'].label = 'Expired'

        # Add CSS classes or other attributes to form fields if needed
        self.fields['job_title'].widget.attrs['class'] = 'form-control'
        self.fields['job_description'].widget.attrs['class'] = 'form-control'
        self.fields['job_role'].widget.attrs['class'] = 'form-control'
        self.fields['job_location'].widget.attrs['class'] = 'form-control'
        self.fields['job_responsibilities'].widget.attrs['class'] = 'form-control'
        self.fields['salary'].widget.attrs['class'] = 'form-control'
        self.fields['job_type'].widget.attrs['class'] = 'form-control'
        self.fields['expired'].widget.attrs['class'] = 'form-control'
