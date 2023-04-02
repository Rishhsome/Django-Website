from pyexpat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Query = models.TextField()
    City = models.CharField(max_length=150)
    PhoneNumber = models.CharField(max_length=15)
    date = models.DateField()

    def __str__(self):
        return self.FirstName