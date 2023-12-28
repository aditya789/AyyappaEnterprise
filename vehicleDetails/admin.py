from datetime import datetime
from django.contrib import admin
from .models import VehicleDetail
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from liststyle import ListStyleAdminMixin
# from rangefilter.filter import DateRangeFilter
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)


admin.site.unregister(Group)


# # Register your models here.

class VehicleDetailsAdmin(ImportExportModelAdmin, ListStyleAdminMixin, admin.ModelAdmin):
    list_display = (
        "Date",
        "Vehicle_Number",
        "Model"
    )
    search_fields = ["Date", "Vehicle_Number", "Model"]

    list_filter = (
        ("Date", DateRangeFilterBuilder()),
    )


admin.site.register(VehicleDetail, VehicleDetailsAdmin)
