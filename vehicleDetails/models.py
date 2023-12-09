from django.db import models

# Create your models here.
class VehicleDetail(models.Model):
    Customer_Name = models.CharField(max_length=100,default=None)
    Contact_Number = models.IntegerField(max_length=15,blank=True,null = True)
    Vehicle_Number = models.CharField(max_length=15)
    Vin_Number = models.CharField(max_length=30)
    Wash_In_Timings = models.DateTimeField(auto_now=False,blank=True,null = True)
    Wash_Out_Timings = models.DateTimeField(auto_now=False,blank=True,null = True)
    Delivery_Time = models.DateTimeField(auto_now=False,blank=True,null = True)
    
    def __str__(self) -> str:
        return f"{self.Vehicle_Number}"