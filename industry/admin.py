from django.contrib import admin
from .models import Type


class IndustryTypeAdmin(admin.ModelAdmin):
    list_display = ('industry_type', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('industry_type',)
    ordering = ('-created_at',)


admin.site.register(Type, IndustryTypeAdmin)
