from django.db import models



# Create your models here.
class Farmers(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     crop1 = models.CharField(max_length=50)
     crop2 = models.CharField(max_length=50)
     crop3 = models.CharField(max_length=50)
     crop4 = models.CharField(max_length=50)
     crop5 = models.CharField(max_length=50)
     state = models.CharField(max_length=50)
     contact = models.CharField(max_length=50)
     username = models.CharField(max_length=50)
     password = models.CharField(max_length=256)

class Customers(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     state = models.CharField(max_length=50)
     contact = models.CharField(max_length=50)
     username = models.CharField(max_length=50)
     password = models.CharField(max_length=256)


     
