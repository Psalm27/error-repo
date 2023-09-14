from django.contrib import admin

# Register your models here.
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name',  'created_at', 'updated_at')
    list_filter = ('course_name', 'created_at', 'updated_at')
    search_fields = ('course_name',)
    ordering = ('-created_at',)


admin.site.register(Course, CourseAdmin)
