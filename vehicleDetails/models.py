from django.db import models


# Create your models here.
class VehicleDetail(models.Model):
    Date = models.DateTimeField(auto_now=True, blank=True, null=True)
    Vehicle_Number = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.Vehicle_Number}"
