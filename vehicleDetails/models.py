from django.db import models

# Create your models here.
class WorkerDetail(models.Model):
    Worker_Name = models.CharField(max_length=40)
    Aadhar_Number = models.IntegerField()
    Address = models.TextField(max_length=200)
    Joined_Date = models.DateTimeField(auto_now=True,null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.Worker_Name}"

class VehicleDetail(models.Model):
    Customer_Name = models.CharField(max_length=100,default=None)
    Contact_Number = models.IntegerField(blank=True,null = True)
    Vehicle_Number = models.CharField(max_length=15)
    Vin_Number = models.CharField(max_length=30)
    Wash_In_Timings = models.DateTimeField(auto_now=False,blank=True,null = True)
    Wash_Out_Timings = models.DateTimeField(auto_now=False,blank=True,null = True)
    Delivery_Time = models.DateTimeField(auto_now=False,blank=True,null = True)
    Worker = models.ForeignKey(WorkerDetail,on_delete=models.PROTECT)
    Remarks = models.TextField(blank=True,null=True)
    Service_Cost = models.IntegerField(blank=True,null=True)
    
    def __str__(self) -> str:
        return f"{self.Vehicle_Number}"