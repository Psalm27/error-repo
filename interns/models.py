from django.conf import settings
from django.db import models

from cv.models import Docs
from joblisting.models import JobPosting


# Create your models here.
class Application(models.Model):
    jobs = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    students = models.ForeignKey(settings.AUTH_USER, on_delete=models.CASCADE)
    cv = models.ForeignKey(Docs, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'student')

    def __str__(self):
        return f"{self.student.last_name}'s application for {self.job.job_title}"