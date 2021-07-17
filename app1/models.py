from django.db import models

# Create your models here.
class Inventory(models.Model):
    Product_Name =  models.CharField("Product Name",max_length=100,default="")
    Item_Code = models.CharField("Item Code",max_length=100,default="")
    Quantity = models.IntegerField("Quantity",default=0)
    Rate = models.IntegerField("Rate",default=0)
    
    def __str__(self):
        return self.Product_Name


class Register(models.Model):
    Name = models.CharField("Name",max_length=100,default="")
    Username = models.EmailField("Username",max_length=100,default="")
    Password = models.CharField("Password",max_length=100,default="")

    def __str__(self):
        return self.Name

class Bill(models.Model):
    C_Name = models.CharField("Customer Name",max_length=100,default="")
    C_Add = models.CharField("Customer Address",max_length=200,default="")
    C_Phone = models.CharField("Customer Number",max_length=10,default="0")
    C_Pro_Name =  models.CharField("Product Name",max_length=100,default="")
    C_Quant = models.IntegerField("Quantity",default=0)

    def __str__(self):
        return self.C_Name