from django.contrib import admin

# Register your models here.
from .models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name',  'created_at', 'updated_at')
    list_filter = ('school_name', 'created_at', 'updated_at')
    search_fields = ('school_name',)
    ordering = ('-created_at',)


admin.site.register(School, SchoolAdmin)
