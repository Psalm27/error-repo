from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Student, Organization

admin.site.register(CustomUser)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'index_number', 'level', 'course', 'school')
    list_filter = ('level', 'course', 'school')
    search_fields = ('first_name', 'last_name', 'index_number')
    ordering = ('last_name', 'first_name')
    fieldsets = ()


admin.site.register(Student, StudentAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry_type')
    list_filter = ('industry_type',)
    search_fields = ('name', 'industry_type__name')
    ordering = ('name',)
    fieldsets = ()


admin.site.register(Organization, OrganizationAdmin)
