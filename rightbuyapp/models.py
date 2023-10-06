from django.db import models

# Create your models here.



from django.db import models

class Login(models.Model):
    phno = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
   

    def __str__(self):
        return f" {self.name}"
    


class BikeType(models.Model):
    
    id = models.AutoField(primary_key=True)
    
    # VARCHAR Field for Name
    name = models.CharField(max_length=100)


class Specification(models.Model):
    
    id = models.AutoField(primary_key=True)
    
    # VARCHAR Field for Name
    name = models.CharField(max_length=250)


class Company(models.Model):
    
    id = models.AutoField(primary_key=True)
    
    # VARCHAR Field for Name
    name = models.CharField(max_length=250)



class Budget(models.Model):
    
    id = models.AutoField(primary_key=True)
    
    # VARCHAR Field for Name
    name = models.CharField(max_length=250)






from django.db import models

class Vehicle(models.Model):
   
    biketype = models.CharField(max_length=250)
    specification = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    budget = models.CharField(max_length=250)
    bikename = models.CharField(max_length=250)
    bikeimage = models.ImageField(upload_to='bike_images/')  # Requires 'Pillow' package

    def __str__(self):
        return f"{self.bikename}"
    

class Scodedetail(models.Model):
    image = models.ImageField(upload_to='bike_images/', blank=True,null=True) 
    heading = models.CharField(max_length=250,blank=True,null=True)
    para =  models.TextField(max_length=250,blank=True,null=True)

    def __str__(self):
        return f"{self.heading}"

