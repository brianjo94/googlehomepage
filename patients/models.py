from django.db import models

# Create your models here.

class PatientName(models.Model):
    """Registering patient name"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

        