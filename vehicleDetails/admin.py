from django.contrib import admin
from .models import VehicleDetail
from django.contrib.auth.models import Group


admin.site.unregister(Group)
# Register your models here.
class VehicleDetailsAdmin(admin.ModelAdmin):
  list_display = ("Customer_Name", "Vehicle_Number", "Contact_Number","Vin_Number","Wash_In_Timings","Wash_Out_Timings","Delivery_Time")
  search_fields  = ["Customer_Name","Vehicle_Number","Vin_Number"]

admin.site.register(VehicleDetail,VehicleDetailsAdmin)