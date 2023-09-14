from django.conf import settings
from django.db import models

# Create your models here.
Jb = (
    ('H', 'Hybrid'),
    ('R', 'Remote'),
    ('Onsite', 'On site'),

)

Ab = (
    ('NS', 'National Service'),
    ('C', 'Contract'),
    ('In', 'Internship'),

)


class JobPosting(models.Model):
    job_title = models.CharField(max_length=200, help_text='eg.Database management System Expert')
    job_description = models.TextField()
    job_role = models.CharField(max_length=100, help_text='Backend Developer')
    job_location = models.CharField(choices=Jb, max_length=100)
    job_responsibilities = models.TextField(blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_type = models.CharField(choices=Ab, max_length=30)
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    expired = models.BooleanField(default=False)
