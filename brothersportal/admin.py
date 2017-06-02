from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.

from .models import Brother


class BrotherResource(resources.ModelResource):

    class Meta:
        model = Brother


class BrotherAdmin(ImportExportModelAdmin):
    resource_class = BrotherResource


admin.site.register(Brother, BrotherAdmin)
