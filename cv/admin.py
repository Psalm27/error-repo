from django.contrib import admin
from .models import Docs


@admin.register(Docs)
class DocsAdmin(admin.ModelAdmin):
    list_display = ('student', 'get_student_email', 'cv', 'cover_letter', 'intro_letter')

    def get_student_email(self, obj):
        return obj.student.email

    get_student_email.short_description = 'Student Email'


