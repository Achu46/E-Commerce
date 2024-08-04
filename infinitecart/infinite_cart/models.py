from django.db import models

# Create your models here.
class users(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    ConfirmPassword=models.CharField(max_length=50)
    DOB=models.DateField(max_length=50)
    Gender=models.CharField(max_length=100)

