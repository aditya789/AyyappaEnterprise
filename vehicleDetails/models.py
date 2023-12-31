from django.db import models


# Create your models here.
class VehicleDetail(models.Model):
    Date = models.DateField(auto_now_add=False)
    Vehicle_Number = models.CharField(max_length=40, )
    Model = models.CharField(max_length=30)

    # To capitalize all the vehicle and Model data
    def save(self, *args, **kwargs):
        for field_name in ['Vehicle_Number', 'Model']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, (val.replace(" ", "")).upper())
        super(VehicleDetail, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.Vehicle_Number}"
