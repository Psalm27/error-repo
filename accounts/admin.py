from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Student, Organization


class CustomUserAdmin(UserAdmin):
    # Specify the field by which you want to order the users
    ordering = ('email',)  # Order by email or any other valid field

    # Specify the fields to display in the admin list view
    list_display = ('email', 'is_active', 'date_joined')

    fieldsets = ()


admin.site.register(CustomUser, CustomUserAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'index_number', 'level', 'course', 'school', 'is_student')
    list_filter = ('level', 'course', 'school', 'is_student')
    search_fields = ('first_name', 'last_name', 'index_number')
    ordering = ('last_name', 'first_name')
    fieldsets = ()


admin.site.register(Student, StudentAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry_type', 'is_organization')
    list_filter = ('industry_type', 'is_organization')
    search_fields = ('name', 'industry_type__name')
    ordering = ('name',)
    fieldsets = ()


admin.site.register(Organization, OrganizationAdmin)
