from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings
import os


def user_cv_upload_to(instance, filename):
    email = instance.student.email
    extension = os.path.splitext(filename)[-1].lower()

    filename = f"{email}_cv{extension}"

    return os.path.join('cv_uploads', filename)


class Docs(models.Model):
    cv = models.FileField(upload_to=user_cv_upload_to, validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
    ])
    cover_letter = models.FileField(upload_to='coverletter_uploads/%Y/%m/%d/', blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
    ])
    intro_letter = models.FileField(upload_to='intro_letter_uploads/%Y/%m/%d/', blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
    ])

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Docs for {self.student.email}"

    class Meta:
        verbose_name = 'Docs'
        verbose_name_plural = 'Docs'


    def save(self, *args, **kwargs):
        if not self.student_id:
            self.student = self._current_user()

        super(Docs, self).save(*args, **kwargs)

    def _current_user(self):
        return self.student
