from django.contrib import admin
from .models import VehicleDetail
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from liststyle import ListStyleAdminMixin

admin.site.unregister(Group)


# Register your models here.
class VehicleDetailsAdmin(ImportExportModelAdmin, ListStyleAdminMixin, admin.ModelAdmin):
    list_display = (
        "Customer_Name",
        "Vehicle_Number",
        "Contact_Number",
        "Vin_Number",
        "Wash_In_Timings",
        "Wash_Out_Timings",
        "Delivery_Time",
    )
    search_fields = ["Customer_Name", "Vehicle_Number", "Vin_Number","Wash_In_Timings"]
    
    def get_row_css(self, obj, index):
        if obj.Delivery_Time:
            return 'green'
        return 'red'


admin.site.register(VehicleDetail, VehicleDetailsAdmin)
