from datetime import datetime
from django.contrib import admin
from .models import VehicleDetail,WorkerDetail
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

from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

admin.site.unregister(Group)


# # Register your models here.
class WorkerDetailsAdmin(ImportExportModelAdmin, ListStyleAdminMixin, admin.ModelAdmin):
    list_display = (
        "Worker_Name",
        "Aadhar_Number",
        "Address",
        "Joined_Date",
    )
    search_fields = ["Worker_Name"]

class VehicleDetailsAdmin(ImportExportModelAdmin, ListStyleAdminMixin, admin.ModelAdmin):
    list_display = (
        "Customer_Name",
        "Vehicle_Number",
        "Contact_Number",
        "Vin_Number",
        "Wash_In_Timings",
        "Wash_Out_Timings",
        "Delivery_Time",
        "Worker",
        "Remarks",
        "Service_Cost"
    )
    search_fields = ["Customer_Name", "Vehicle_Number", "Vin_Number","Delivery_Time"]
   
    # list_filter = (
    #     # for ordinary fields
    #     ('a_charfield', DropdownFilter),
    #     # for choice fields
    #     ('a_choicefield', ChoiceDropdownFilter),
    #     # for related fields
    #     ('a_foreignkey_field', RelatedDropdownFilter),
    # )
    
    list_filter = (
        ("Worker", RelatedDropdownFilter),
        ("Wash_In_Timings", DateRangeFilterBuilder()),
        ("Wash_Out_Timings", DateRangeFilterBuilder()),
        ("Delivery_Time", DateRangeFilterBuilder()), 
    )

admin.site.register(WorkerDetail, WorkerDetailsAdmin)
admin.site.register(VehicleDetail, VehicleDetailsAdmin)
