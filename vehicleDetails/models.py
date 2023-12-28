from django.db import models


# Create your models here.
class VehicleDetail(models.Model):
    Date = models.DateField(auto_now_add=False)
    Vehicle_Number = models.CharField(max_length=40)
    Model = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.Vehicle_Number}"
